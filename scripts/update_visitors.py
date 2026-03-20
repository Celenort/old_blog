#!/usr/bin/env python3
"""
update_visitors.py
---------------------------------
Fetches cloudflared Prometheus metrics (HTTP endpoint)
→ Sums all `cloudflared_tunnel_response_by_code` counts (status 200/304/404 etc.)
→ Computes daily delta from saved state (no sudo required)
→ Writes JSON {"today": N, "total": M} to data/visitors.json
→ Logs timestamp + today/total counters to log file.

Intended to run via cron every few minutes.
"""

import os
import sys
import json
import re
from datetime import datetime, timezone, timedelta
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# ===== CONFIG =====
BASE_DIR = os.path.expanduser("/home/celenort/repos/jekyll-theme-instagram")
METRICS_URL = "http://127.0.0.1:36500/metrics"
OUT_FILE = os.path.join(BASE_DIR, "data/visitors.json")
STATE_FILE = os.path.join(BASE_DIR, "scripts/visitors_state.json")
LOG_FILE = os.path.join(BASE_DIR, "scripts/update_visitors.log")
TZ_OFFSET_HOURS = 9  # UTC+9 for Korea
# ==================

def log(msg: str):
    ts = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")

def fetch_metrics(url: str, timeout: int = 5) -> str:
    req = Request(url, headers={"User-Agent": "update-visitors-script/1.1"})
    with urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")

def parse_total_requests(metrics_text: str) -> int:
    """
    Sum all values from `cloudflared_tunnel_response_by_code`
    Fallback to other possible counters if not found.
    """
    total = 0
    found = False
    for line in metrics_text.splitlines():
        if line.startswith("cloudflared_tunnel_response_by_code"):
            m = re.search(r"\s+([0-9]+(?:\.[0-9]+)?)\s*$", line)
            if m:
                total += int(float(m.group(1)))
                found = True
    if found:
        return total

    # fallback: cloudflared_tunnel_total_requests
    for line in metrics_text.splitlines():
        if line.startswith("cloudflared_tunnel_total_requests"):
            m = re.search(r"\s+([0-9]+(?:\.[0-9]+)?)\s*$", line)
            if m:
                total += int(float(m.group(1)))
                found = True
    if found:
        return total

    # last resort: any cloudflared line with trailing number
    for line in metrics_text.splitlines():
        if line.startswith("cloudflared"):
            m = re.search(r"\s+([0-9]+(?:\.[0-9]+)?)\s*$", line)
            if m:
                total += int(float(m.group(1)))
                found = True
    return total

def get_today_date_str() -> str:
    local = datetime.now(timezone.utc) + timedelta(hours=TZ_OFFSET_HOURS)
    return local.strftime("%Y-%m-%d")

def load_state() -> dict:
    if not os.path.exists(STATE_FILE):
        return {}
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_state(state: dict):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f)
    os.replace(tmp, STATE_FILE)

def write_output(today_count: int, total_count: int):
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    tmp = OUT_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"today": today_count, "total": total_count}, f)
    os.replace(tmp, OUT_FILE)

def main() -> int:
    try:
        metrics = fetch_metrics(METRICS_URL)
    except Exception as e:
        log(f"ERROR: failed to fetch metrics ({e})")
        return 1

    current_total = parse_total_requests(metrics)
    if current_total <= 0:
        log(f"WARN: no valid request metrics found (current_total={current_total})")
        return 0

    state = load_state()
    last_date = state.get("date", "")
    daily_start = int(state.get("daily_start", 0))
    last_total = int(state.get("last_total", 0))
    today = get_today_date_str()

    # day change → reset daily_start
    if last_date != today:
        daily_start = current_total

    # cloudflared restart → counter reset
    if current_total < last_total:
        log(f"INFO: detected counter reset (current {current_total} < last {last_total})")
        daily_start = current_total

    today_count = max(current_total - daily_start, 0)

    # save state & write output
    save_state({"date": today, "daily_start": daily_start, "last_total": current_total})
    write_output(today_count, current_total)

    log(f"OK: visitors updated → today={today_count}, total={current_total}")
    return 0

if __name__ == "__main__":
    sys.exit(main())


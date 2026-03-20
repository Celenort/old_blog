# 📚 찬진의 독서 기록 (Instagram-style Jekyll Site)

이 프로젝트는 **Jekyll** 기반의 정적 웹사이트로,  
인스타그램 피드 형식으로 책 리뷰(독후감)를 표시합니다.

---

## 🚀 기능

- 5열 고정 A4비율 갤러리 (반응형)
- 게시글 클릭 시 모달 팝업으로 상세 보기
- 좌우 화살표 또는 키보드로 이전/다음 탐색
- 방문자 수 표시 (Today / Total)
- 정적 사이트 빌드 후 바로 호스팅 가능

---

## 📂 폴더 구조

```
mysite/
├── _config.yml
├── _layouts/
│   ├── default.html
│   └── home.html
├── _includes/
│   └── profile.html
├── assets/
│   ├── css/style.scss
│   └── js/
│       ├── modal.js
│       └── visitor.js
├── _posts/
│   └── YYYY-MM-DD-책제목.md
└── index.html
```

---

## 🧱 설치 및 빌드

```bash
bundle install --path vendor/bundle
bundle exec jekyll build
```

빌드된 결과는 `_site/` 폴더에 저장됩니다.

---

## 🌍 로컬 서버 실행

```bash
bundle exec jekyll serve --host 0.0.0.0 --port 8080
```

혹은 Python으로 바로 확인:
```bash
cd _site
python3 -m http.server 8080
```

---

## 🧠 추가 참고

- `_posts/` 폴더에 Markdown 파일을 추가하면 새 게시글로 자동 반영됩니다.
- `assets/js/modal.js`에서 팝업 동작과 URL 히스토리 관리 기능을 확인할 수 있습니다.
- `assets/js/visitor.js`는 localStorage 기반의 방문자 카운터를 제공합니다.

---

© 2025 김찬진. All rights reserved.

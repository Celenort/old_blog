---
title: "Lifestyle"
layout: archive
permalink: categories/life
author_profile: true
sidebar_main: true
---

#### 학업 외 게시물 (스터디, 음악, 기타등등)

{% assign posts = site.categories.life %}
{% for post in posts %} {% include archive-single2.html type=page.entries_layout %} {% endfor %}
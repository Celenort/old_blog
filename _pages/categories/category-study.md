---
title: "Study"
layout: archive
permalink: categories/study
author_profile: true
sidebar_main: true
---

#### 학업 관련 게시물(대학 교과목)

{% assign posts = site.categories.study %}
{% for post in posts %} {% include archive-single2.html type=page.entries_layout %} {% endfor %}
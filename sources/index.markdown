---
layout: page
title: sources
order: 4
---

<script async src="https://www.googletagmanager.com/gtag/js?id=G-38882FHV3H"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-38882FHV3H');
</script>

{% include_relative styles-local.html %}
{% include_relative scripts-local.html %}
{% include styles/styles-common.css.html %}

<div class="section-header"><h4 data-i18n="src.heading">Sources</h4></div>

<div id="sources-cards"></div>

<div id="source-works-panel" class="source-works-hidden">
  <div id="source-works-header"></div>
  <div id="source-search-bar">
    <input type="text" id="source-input" onkeyup="sourceSearch()" placeholder="Filter by title, composer…" data-i18n-placeholder="src.search_placeholder">
    <span id="source-count"></span>
  </div>
  <div id="source-works-list"></div>
</div>

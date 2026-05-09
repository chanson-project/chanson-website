---
layout: work
---

{% include_relative styles-local.html %}

<script async src="https://www.googletagmanager.com/gtag/js?id=G-38882FHV3H"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-38882FHV3H');
</script>

<audio id="audio"></audio>

<table id="work-info">
   <thead>
       <tr>
           <th class="left-column">Left Column</th>
           <th class="middle-column">Middle Column</th>
           <th class="right-column">Right Column</th>
       </tr>
   </thead>
   <tbody id="work-info-body"></tbody>
</table>

<div id="external-info"></div>

<div id="search-nav" class="hidden">
  <button class="button nav-btn" id="nav-prev" onclick="navigateSearchResult(-1)">&#9664;</button>
  <span id="nav-position"></span>
  <button class="button nav-btn" id="nav-next" onclick="navigateSearchResult(1)">&#9654;</button>
  <a id="nav-back-link" href="/repertoire/" class="button nav-btn">&#8592; Search</a>
</div>

<div id="button-container" class="button-container">
    <div id="audiobutton-container">
        <span id="audiobutton-play" class="play">play</span>
    </div>
    <div id="textSelect">
       <div class="button show-text" onclick="displayText()" data-i18n="work.show_text">Show Text</div>
    </div>
</div>

<script type="text/x-humdrum" id="my-score"></script>

<div id="work-footer"></div>

{% include_relative listeners.html %}
{% include_relative scripts-local.html %}
{% include_relative scripts-player.html %}
{% include styles/svgdefs.html %}
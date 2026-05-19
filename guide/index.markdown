---
layout: page
title: guide
---

{% include styles/styles-common.css.html %}
{% include_relative styles-local.html %}

<div class="section-header"><h4 data-i18n="guide.heading">User Guide</h4></div>

<div class="guide-container">

  <div class="guide-lang" id="guide-en">

    <h2>Browsing the Repertoire</h2>
    <p>The <a href="/repertoire/">Chansons</a> page lists all works in the database. You can narrow the list using the search bar, melodic search, or the dropdown filters.</p>

    <h3>Text Search</h3>
    <p>Type in the search box to filter by <strong>title</strong>, <strong>composer</strong>, or <strong>lyricist</strong>. The search is accent-insensitive, so <em>noel</em> will match <em>Noël</em>.</p>

    <h3>Melodic Search</h3>
    <p>Use the melodic search box to find works by a sequence of notes. You can search in two ways:</p>
    <ul>
      <li><strong>Pitch names</strong> — enter note names separated by spaces, e.g. <code>G A F# E</code>. Use <code>#</code> for sharps and <code>b</code> for flats.</li>
      <li><strong>Scale degrees</strong> — enter scale degree numbers separated by spaces, e.g. <code>1 2 3 6 5</code>. Use <code>#</code> or <code>b</code> as prefixes for chromatic alterations, e.g. <code>#4</code> or <code>b7</code>. Degrees are relative to the key of each work.</li>
    </ul>
    <p>At least two tokens are required. Matching works are highlighted in the results table, and when you open a work, the matching notes are highlighted in the score.</p>

    <h3>Dropdown Filters</h3>
    <p>Use the dropdown menus to filter by <strong>Composer</strong>, <strong>Lyricist</strong>, <strong>Origin</strong>, <strong>Collection</strong>, or <strong>Editor</strong>. Each menu shows the number of distinct values in the current dataset. Multiple filters can be active at once.</p>

    <h3>Show Variants</h3>
    <p>Check <strong>Show variants</strong> to include variant versions of works (works whose ID ends in a letter).</p>

    <h3>Clear All</h3>
    <p>Click <strong>Clear All</strong> to reset all filters and search fields at once. You can also press <kbd>Delete</kbd> or <kbd>Backspace</kbd> while the text search box is empty.</p>

    <h3>Sources</h3>
    <p>The <strong>Sources</strong> menu in the navigation bar lets you jump directly to works from a particular source collection.</p>

    <hr>

    <h2>Viewing a Work</h2>
    <p>Click any row in the results table to open the score for that work.</p>

    <h3>Audio Playback</h3>
    <p>Click <strong>Play</strong> to hear a MIDI rendering of the score. Click again to pause.</p>

    <h3>Show Text</h3>
    <p>Click <strong>Show Text</strong> to display the song lyrics beneath the score. Click <strong>Hide Text</strong> to collapse them.</p>

    <h3>Navigating Search Results</h3>
    <p>When you arrive at a work from a search, <strong>◀</strong> and <strong>▶</strong> buttons appear at the top of the page to step through all matching results in order. The current position (e.g. <em>3 / 12</em>) is shown between the buttons. You can also use the <kbd>←</kbd> and <kbd>→</kbd> arrow keys. Click <strong>← Search</strong> to return to the search results.</p>

    <h3>Melodic Highlighting</h3>
    <p>If you arrived via a melodic search, the matching notes are highlighted in colour directly on the score.</p>

  </div>

  <div class="guide-lang" id="guide-fr" style="display:none">

    <h2>Parcourir le répertoire</h2>
    <p>La page <a href="/repertoire/">Chansons</a> liste toutes les œuvres de la base de données. Vous pouvez affiner la liste avec la barre de recherche, la recherche mélodique ou les menus déroulants.</p>

    <h3>Recherche textuelle</h3>
    <p>Saisissez du texte dans le champ de recherche pour filtrer par <strong>titre</strong>, <strong>compositeur</strong> ou <strong>auteur</strong>. La recherche est insensible aux accents : <em>noel</em> trouvera <em>Noël</em>.</p>

    <h3>Recherche mélodique</h3>
    <p>Utilisez le champ de recherche mélodique pour trouver des œuvres par une séquence de notes. Deux modes sont disponibles :</p>
    <ul>
      <li><strong>Noms de notes</strong> — saisissez des noms de notes séparés par des espaces, p. ex. <code>G A F# E</code>. Utilisez <code>#</code> pour les dièses et <code>b</code> pour les bémols.</li>
      <li><strong>Degrés</strong> — saisissez des degrés de gamme séparés par des espaces, p. ex. <code>1 2 3 6 5</code>. Utilisez <code>#</code> ou <code>b</code> comme préfixes pour les altérations chromatiques. Les degrés sont relatifs à la tonalité de chaque œuvre.</li>
    </ul>
    <p>Au moins deux éléments sont requis. Les œuvres correspondantes sont mises en évidence dans le tableau, et à l'ouverture d'une œuvre, les notes correspondantes sont surlignées dans la partition.</p>

    <h3>Menus déroulants</h3>
    <p>Utilisez les menus pour filtrer par <strong>Compositeur</strong>, <strong>Auteur</strong>, <strong>Origine</strong>, <strong>Collection</strong> ou <strong>Éditeur</strong>. Chaque menu indique le nombre de valeurs distinctes dans le jeu de données courant. Plusieurs filtres peuvent être actifs simultanément.</p>

    <h3>Afficher les variantes</h3>
    <p>Cochez <strong>Afficher les variantes</strong> pour inclure les versions variantes des œuvres (dont l'identifiant se termine par une lettre).</p>

    <h3>Tout effacer</h3>
    <p>Cliquez sur <strong>Tout effacer</strong> pour réinitialiser tous les filtres et champs de recherche. Vous pouvez aussi appuyer sur <kbd>Suppr</kbd> ou <kbd>Retour arrière</kbd> lorsque le champ de recherche est vide.</p>

    <h3>Sources</h3>
    <p>Le menu <strong>Sources</strong> dans la barre de navigation vous permet d'accéder directement aux œuvres d'une collection particulière.</p>

    <hr>

    <h2>Consulter une œuvre</h2>
    <p>Cliquez sur n'importe quelle ligne du tableau pour ouvrir la partition.</p>

    <h3>Lecture audio</h3>
    <p>Cliquez sur <strong>Écouter</strong> pour entendre un rendu MIDI de la partition. Cliquez à nouveau pour mettre en pause.</p>

    <h3>Afficher le texte</h3>
    <p>Cliquez sur <strong>Afficher le texte</strong> pour afficher les paroles sous la partition. Cliquez sur <strong>Masquer le texte</strong> pour les replier.</p>

    <h3>Navigation dans les résultats</h3>
    <p>Lorsque vous accédez à une œuvre depuis une recherche, les boutons <strong>◀</strong> et <strong>▶</strong> apparaissent en haut de la page pour parcourir tous les résultats correspondants. La position courante (p. ex. <em>3 / 12</em>) est indiquée entre les boutons. Vous pouvez aussi utiliser les touches <kbd>←</kbd> et <kbd>→</kbd>. Cliquez sur <strong>← Recherche</strong> pour revenir aux résultats.</p>

    <h3>Surlignage mélodique</h3>
    <p>Si vous êtes arrivé via une recherche mélodique, les notes correspondantes sont surlignées en couleur directement sur la partition.</p>

  </div>

</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  function updateGuideLang() {
    var lang = window.LANG || "en";
    document.getElementById("guide-en").style.display = (lang === "fr") ? "none" : "";
    document.getElementById("guide-fr").style.display = (lang === "fr") ? "" : "none";
  }
  updateGuideLang();
  document.addEventListener("langchange", updateGuideLang);
});
</script>

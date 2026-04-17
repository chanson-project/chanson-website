# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Local development:**
```bash
bundle exec jekyll serve --incremental --trace --watch --port 8888
# or simply:
cat .serve   # contains the full command
```

**Sync metadata from Google Sheets:**
```bash
make         # fetches JSON files into _includes/metadata/
```

**Production build:**
```bash
bundle exec jekyll build
```

Deployment is automatic via GitHub Actions on push to `main` — the workflow runs `make` then `bundle exec jekyll build` and deploys to GitHub Pages at `1520s-project.org`.

## Architecture

This is a Jekyll static site for an academic musicology database (Renaissance polyphony ca. 1510–1540). The site is largely static HTML/CSS/JS with client-side search — no server-side logic.

### Data flow

The live data source is a Google Spreadsheet exposed via a deployed Google Apps Script. `make` curls that endpoint to download `_includes/metadata/works.json`. This file is embedded directly into HTML at Jekyll build time using a Liquid `{% include %}` tag, becoming a JavaScript variable at page load:

```javascript
let METADATA = {% include metadata/works.json %};
```

All search and filtering is client-side JavaScript operating on those in-memory objects.

### Page structure

Each page directory (e.g., `repertoire/`, `about/`, `work/`) contains:
- `index.markdown` — Markdown front matter + Liquid template body
- `scripts-local.html` — page-specific JavaScript included via Liquid
- `scripts-listeners.html` — event handlers / data binding
- `styles-local.html` — page-specific CSS

Global includes live in `_includes/` (header, footer, shared scripts/styles). The single work detail page uses `_layouts/work.html`.

### Search/filter (repertoire page)

URL parameters drive the search state: `?c=` (composer), `?o=` (origin), `?x=` (text availability), `?q=` (free text). Parsed via `_includes/scripts/getCgiParameters.js`. Dropdowns are built dynamically from METADATA; filtering is pure client-side.
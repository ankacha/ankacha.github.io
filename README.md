# ankacha.github.io

A landing page for a small family of self-contained, browser-based structural engineering tools. Each tool is a single HTML file — nothing to install, nothing to sign in to — and runs on a laptop, tablet or phone.

**Live site:** https://ankacha.github.io

## Projects

| Project | Path | What it does |
|---|---|---|
| **Frame Pusher** | [`/frame-pusher`](https://ankacha.github.io/frame-pusher) | Interactive 2D frame finite-element analysis with a steel section library, supports, loads, end releases, bending moment / shear / deflection diagrams and a live view of the assembled stiffness matrix. |
| **Arch Pusher** | [`/arch-pusher`](https://ankacha.github.io/arch-pusher) | Lower-bound thrust-line analysis of masonry arches, vaults and domes, including multi-ring brick arches, bonding and ring separation. |
| **Cable Pusher** | [`/cable-pusher`](https://ankacha.github.io/cable-pusher) | Cable and tension structures from first principles — catenary shape, sag, horizontal thrust and cable tension under point and distributed loads. |
| **Lintel Loader** | [`/lintel-loader`](https://ankacha.github.io/lintel-loader) | Masonry lintel and pier design to EC6 / EC3 / EC2 (UK NA): arching action and load triangles, steel, concrete or proprietary lintels, bearing and pier checks, and a PDF calculation sheet. |
| **Codex Structura** | [`/codex-structura`](https://ankacha.github.io/codex-structura) | Timeline and lineage explorer for historic British structural standards and codes of practice, to support appraisal and reuse of existing structures. |

## Repository layout

```
ankacha.github.io/
├── index.html              ← this landing page
├── README.md
├── frame-pusher/
│   └── index.html
├── arch-pusher/
│   └── index.html
├── cable-pusher/
│   └── index.html
├── lintel-loader/
│   └── index.html
└── codex-structura/
    └── index.html
```

Each tool lives in its own folder as `index.html`, so GitHub Pages serves it at `ankacha.github.io/<folder>/`. The landing page links to each folder with a relative path (`frame-pusher/`, `lintel-loader/`, …), so the site also works when opened locally.

## Publishing on GitHub Pages

1. Create a public repository named exactly **`ankacha.github.io`**.
2. Commit `index.html`, `README.md` and the project folders to the `main` branch.
3. In the repository, go to **Settings → Pages** and set **Source** to *Deploy from a branch*, branch `main`, folder `/ (root)`.
4. After a minute or so the site is live at https://ankacha.github.io.

```bash
git clone https://github.com/ankacha/ankacha.github.io.git
cd ankacha.github.io
# copy in index.html, README.md and the project folders
git add .
git commit -m "Landing page v1.1: add Lintel Loader"
git push origin main
```

## Running locally

No build step. Open `index.html` directly in a browser, or serve the folder so the relative links behave exactly as on GitHub Pages:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Adding a new project

1. Put the tool's single HTML file in a new folder as `<project-name>/index.html`.
2. In the landing page `index.html`:
   - add a link to the top-bar `<nav>`;
   - copy one of the `<a class="card">` blocks inside `<section class="grid">`, then update its `href`, tag, title, description and the `ankacha.github.io/<project-name>` line;
   - draw the card illustration as inline SVG in the `320 × 180` view box, using the shared palette classes (`.ink`, `.ac`, `.cy`, `.mg`, `.fa`, `.fc`, `.fm`, `.fp`, `.tx`, `.tk`) so it follows the light and dark themes.
3. Add the project to the table above and bump the version in the top bar, `<title>` and footer.

If the number of cards is odd, the last card automatically spans the full width on desktop, with its illustration beside the text.

## Design notes

- Shared "Frame Pusher family" cyberpunk theme: purple / magenta / cyan neon accents with matching light and dark palettes.
- Dark theme by default; the moon button toggles light / dark and the choice is remembered in the browser (`localStorage` key `ankacha-theme`).
- No external dependencies: fonts fall back to the system stack, icons and illustrations are inline SVG, and the favicon is a data URI.
- Animations respect `prefers-reduced-motion`.

## Changelog

- **v1.1** — Added the Lintel Loader card and nav link; an odd last card now spans the full width on desktop.
- **v1.0** — First release: Frame Pusher, Arch Pusher, Cable Pusher and Codex Structura.

## Disclaimer

These are educational tools. Always check results independently before using them in design.

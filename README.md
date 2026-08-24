# Academic website — S M (Rifat) Rafiuddin

This repository contains a single-page, faculty-search-focused academic website for GitHub Pages. Its layout is adapted from [Minimal Light](https://github.com/yaoyao-liu/minimal-light), with the original portfolio's section structure, monospace typography, institutional logos, detailed academic content, and PhD Comics feature.

## Publish on GitHub Pages

1. Replace the contents of the copotronicrifat.github.io repository with the contents of this folder.
2. Commit and push to the repository's default branch.
3. In Settings → Pages, select Deploy from a branch, then choose the default branch and the repository root.
4. Allow GitHub Pages a few minutes to rebuild the site.

## Site structure

- Homepage and all visible content: index.md
- Publication records: _data/publications.yml
- Publication component: _includes/publications.html
- Profile, icon links, and navigation: _layouts/homepage.html
- Identity, profile URLs, and metadata: _config.yml
- Styling: assets/css/style.css
- Current CV: assets/files/Rifat_Rafiuddin_CV.pdf

Navigation uses same-page anchors:

About → News → Education → Experience → Publications → Projects and Research → Misc Links → Contact

## Local preview

Run bundle install, followed by bundle exec jekyll serve.

# Academic website — S M (Rifat) Rafiuddin

This repository contains a faculty-search-focused academic website for GitHub Pages. Its visual structure is adapted from [Minimal Light](https://github.com/yaoyao-liu/minimal-light), with custom content architecture, typography, responsive behavior, and publication components.

## Publish on GitHub Pages

1. Replace the contents of the `copotronicrifat.github.io` repository with the contents of this folder.
2. Commit and push to the repository's default branch.
3. In **Settings → Pages**, select **Deploy from a branch**, then choose the default branch and `/ (root)`.
4. Allow GitHub Pages a few minutes to build the site.

## Edit content

- Homepage: `index.md`
- Publication records: `_data/publications.yml`
- Full publication page: `publications.md`
- Teaching and mentoring: `teaching.md`
- Research/software projects: `projects.md`
- News archive: `news.md`
- PhD Comics and personal links: `personal.md`
- Identity, links, and metadata: `_config.yml`
- Site styling: `assets/css/style.css`

The current CV is stored at `assets/files/Rifat_Rafiuddin_CV.pdf`.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

Then open the local address printed by Jekyll.

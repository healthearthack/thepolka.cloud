# Canonical Master Decision

The August 14, 2026 `thepolka.cloud-USE-ME` archive was selected as the source because it contained the fullest site, sub-app collection, extension card, and shared presentation system.

This repository is the definitive source going forward. Work should branch from `main` here instead of modifying archived ZIP files or the older `https-thepolka.cloud` repositories.

## Preserved

- Root Flask site, templates, imagery, CSS, and JavaScript
- Active product and sub-app source
- ThePolka Chrome Extension discovery card
- Ghost Agent product, local source, tests, download, and interactive walkthrough
- Historical documentation that remains useful

## Excluded from publication

- The 95 MB nested source archive
- `__pycache__`, `.pyc`, databases, virtual environments, and runtime instance data
- `.OLD`, `.backup`, and duplicate archived app trees
- Real Cloudflare tunnel configuration and local credential paths
- Hardcoded demonstration passwords

The exclusions reduce the repository from roughly 97 MB extracted to a small, reviewable source tree without removing active product code.

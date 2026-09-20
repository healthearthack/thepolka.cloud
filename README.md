# 🌐 thepolka.cloud (`thepolka.cloud`)
**Public Web Portal, Google City Cloud 3D Engine & W3C-Validated RSS 2.0 Research Syndication Hub**
*Part of the 6-Repository Cyber-Physical Energy Research Suite (`@healthearthack`)*

[![Syndicate RSS & Portal CI/CD](https://github.com/healthearthack/thepolka.cloud/actions/workflows/syndicate_rss.yml/badge.svg)](https://github.com/healthearthack/thepolka.cloud/actions)
[![RSS 2.0 Validated](https://img.shields.io/badge/RSS%202.0-W3C%20Validated-orange.svg)](feed.xml)
[![Live Portal](https://img.shields.io/badge/Live%20Portal-go.thepolka.cloud-brightgreen.svg)](https://go.thepolka.cloud)
[![Domain: thepolka.cloud](https://img.shields.io/badge/Domain-thepolka.cloud-blue.svg)](https://thepolka.cloud)

---

## 🏛️ Mission & Architecture
`thepolka.cloud` operates as **Puzzle Piece #6**: the global syndication anchor and commercial web portal for Metaknews LLC. It bridges high-density academic research, enterprise capabilities, and consumer-facing 3D interactive experiences:

1. **W3C-Validated RSS 2.0 Feed (`feed.xml`)**:
   - Ingests newly minted research monographs and DOIs from `industrial-research-publisher`.
   - Distributes full metadata, abstracts, BibTeX links, and PDF download links to institutional aggregators, search engine indexers, and academic libraries worldwide.
2. **Google City Cloud 3D Digital Advertising Portal**:
   - Live 3D isometric city engine (`portal/index.html` / `go.thepolka.cloud`).
   - Integrated Google Partner Program member disclosures (`portal/guide.html`) and statutory CYA protections.
   - Interactive Mission Control CRM (`portal/helm.html`) and real-time telemetry simulator.
3. **Express TypeScript Microservice**:
   - Fast Node/Express server (`src/server.ts`) capable of edge deployment on Cloudflare Workers, Vercel, or standalone Linux/Docker hosts.

---

## 📡 Live Syndication Endpoints
* **RSS 2.0 Feed**: `https://thepolka.cloud/feed.xml`
* **Official Web Portal**: `https://go.thepolka.cloud`
* **Executive Mission Control**: `https://go.thepolka.cloud/helm.html`
* **Google Partner Transparency Guide**: `https://go.thepolka.cloud/guide.html`

---

## 📂 Repository Structure
```
thepolka.cloud/
├── README.md                              # Portal & syndication architecture monograph
├── update_feed.py                         # Python automated RSS 2.0 XML generator
├── feed.xml                               # W3C-valid RSS 2.0 publication feed
├── pyproject.toml                         # Python packaging
├── package.json                           # Express & TypeScript microservice
├── src/
│   ├── feed_types.ts                      # TypeScript types for RSS 2.0 items
│   └── server.ts                          # Express server for portal & RSS delivery
├── notebooks/
│   └── traffic_and_citation_telemetry.ipynb # Doctoral Jupyter Notebook for citation analytics
├── public/                                # Static web portal assets (from portal/)
│   ├── index.html                         # Google City Cloud 3D Portal
│   ├── helm.html                          # Mission Control CRM Dashboard
│   ├── guide.html                         # Google Partner Program CYA Guide
│   └── CNAME                              # go.thepolka.cloud
└── .github/
    └── workflows/
        └── syndicate_rss.yml              # Automated GitHub Pages / syndication CI/CD
```

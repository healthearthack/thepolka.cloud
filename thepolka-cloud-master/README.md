# ThePolka.Cloud

This is the definitive, publishable master for **thepolka.cloud**. It consolidates the August 14, 2026 “USE-ME” archive into one maintainable Flask workspace and restores Ghost Agent as a real downloadable local product.

**Canonical repository:** `healthearthack/thepolka.cloud`  
**Canonical branch:** `main`  
**Local site:** `http://127.0.0.1:8001`

## What works

- ThePolka.Cloud product and app library
- Ghost Agent product page, interactive walkthrough, and source download
- ThePolka Chrome Extension card for extension ID `enibnbffggiaglilabcmpldlmlalmigm`
- Health endpoint at `/health`
- Preserved Flask sub-app source for CAD, directory, Faire, mail, privacy, résumé, store, and X experiments

## Run the website

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py app.py
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py
```

Open `http://127.0.0.1:8001`, choose **Ghost Agent**, and run the `2+2` walkthrough.

## Run the downloaded Ghost Agent

1. From the site, select **Download version 1.0.0**.
2. Extract `ghost-agent-v1.0.0-source.zip`.
3. In Windows PowerShell, run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\run.ps1
```

4. Enter `2+2`, `:wait`, and `:tail 10`.

Ghost Agent is a zero-dependency Python command-line interface. It performs safe bounded arithmetic and writes a transparent background planning ledger to `~/.ghost/stream.log`. It has no remote application programming interface, telemetry, shell execution, or hidden background service.

## Product map

| Product | Location | Status |
|---|---|---|
| Main site | `app.py`, `templates/`, `static/` | Canonical |
| Ghost Agent | `products/ghost-cli/` | Working v1.0.0 |
| Résumé generator | `resume-generator.thepolka.cloud/` | Preserved sub-app |
| App experiments | `*.thepolka.cloud/`, `directory-app/` | Preserved source |

## Deployment

Run the main process with `gunicorn app:app`. A Cloudflare Tunnel example is provided in `cloudflared-tunnel.example.yml`; keep the real tunnel UUID and credentials file outside Git.

## Security and repository hygiene

The canonical master intentionally excludes nested archives, runtime databases, Python caches, virtual environments, backup applications, local tunnel credentials, and published passwords. Optional X demo logins must be supplied at runtime through `THEPOLKA_X_USERS_JSON`; use hashed identity storage before treating that experiment as production authentication.

See [CANONICAL.md](CANONICAL.md) for the merge decision and excluded material.

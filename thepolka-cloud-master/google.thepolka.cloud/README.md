# google.thepolka.cloud

Run locally:

```powershell
cd .\thepolka-cloud-master\google.thepolka.cloud
python -m pip install -r requirements.txt
python .\app.py
```

Default port: `8016`.

Cloudflare Tunnel ingress:

```yaml
- hostname: google.thepolka.cloud
  service: http://localhost:8016
```

The #GrowWithGoogle watch is a best-effort Google News RSS feed, not a comprehensive social ranking.

"""Canonical thepolka.cloud root application."""

import os

from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

# Spell archive
app = Flask(__name__, template_folder="templates", static_folder="static")
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/apps/ghost-agent")
def ghost_agent():
    return render_template("ghost-agent.html")


@app.route("/health")
def health():
    return {"status": "ok", "service": "thepolka.cloud"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8001"))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

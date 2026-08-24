from __future__ import annotations
import os, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from flask import Flask, jsonify, render_template

app = Flask(__name__)

GOOGLE_LINKS = [
    ("Google Account","https://myaccount.google.com/","Security, privacy, devices, payments, and account controls."),
    ("Account Chooser","https://accounts.google.com/AccountChooser","Switch between your Google identities."),
    ("Gmail","https://mail.google.com/","Inbox, drafts, labels, and the human approval queue."),
    ("Google Drive","https://drive.google.com/","Documents, datasets, research, and project artifacts."),
    ("Google Calendar","https://calendar.google.com/","Schedule, review windows, and project planning."),
    ("Gemini","https://gemini.google.com/","Google's Gemini assistant."),
    ("Google AI Studio","https://aistudio.google.com/","Prototype prompts and Gemini API workflows."),
    ("Google Cloud Console","https://console.cloud.google.com/","Cloud projects, APIs, IAM, logs, and billing."),
    ("Google Colab","https://colab.research.google.com/","Hosted Python notebooks."),
    ("YouTube Studio","https://studio.youtube.com/","Publishing, analytics, and channel operations."),
    ("Search Console","https://search.google.com/search-console","Indexing and search performance."),
    ("Google Analytics","https://analytics.google.com/","Web traffic and audience analytics."),
    ("Grow with Google","https://grow.google/","Training, certificates, and career resources."),
]

PROMPTS = [
    ("Gmail Draft Agent","Gmail + Gemini","Read this email thread, identify the sender's actual request, list commitments or deadlines, and draft a concise reply. Do not send. Flag anything requiring human judgment."),
    ("Drive Research Synthesizer","Drive + Gemini","Synthesize the strongest evidence across these documents. Separate verified facts, assumptions, unresolved questions, and the next three actions. Cite the source document for every material claim."),
    ("Calendar Operator","Calendar + Gemini","Review this week's calendar and propose a schedule that protects deep-work blocks, groups administrative work, and leaves realistic transition time. Do not modify events until I approve."),
    ("Sheets Decision Analyst","Sheets + Gemini","Analyze this sheet for trends, anomalies, missing values, and decision-relevant relationships. Explain which conclusions are supported and which require more evidence."),
    ("Google Ecosystem Builder","Gemini + Cloud","Turn this product idea into a minimal Google-native architecture. Prefer the fewest services necessary, identify authentication and privacy boundaries, and give me the first implementation step."),
]

def fetch_activity(limit=5):
    q = urllib.parse.quote('"Grow with Google" OR #GrowWithGoogle')
    url = f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"
    req = urllib.request.Request(url, headers={"User-Agent":"google.thepolka.cloud/1.0"})
    with urllib.request.urlopen(req, timeout=5) as r:
        root = ET.fromstring(r.read())
    out=[]
    for item in root.findall("./channel/item")[:limit]:
        src=item.find("source")
        out.append({
            "title": item.findtext("title","Grow with Google mention"),
            "url": item.findtext("link","https://grow.google/"),
            "source": src.text if src is not None and src.text else "Public web",
        })
    return out

@app.get("/")
def home():
    return render_template("index.html", links=GOOGLE_LINKS, prompts=PROMPTS)

@app.get("/api/activity")
def activity():
    try:
        return jsonify({"ok":True,"items":fetch_activity()})
    except Exception:
        return jsonify({"ok":False,"items":[]})

@app.get("/health")
def health():
    return {"status":"ok","service":"google.thepolka.cloud"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT","8016")), debug=False)

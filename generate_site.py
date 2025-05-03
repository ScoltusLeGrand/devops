#!/usr/bin/env python3
"""
Générateur auto de site DevOps
"""
from datetime import datetime
import sys
from pathlib import Path

CONFIG = {
    "title": "Projet DevOps",
    "color": "#E67E22",
    "author": "Bernard Thibaut"
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="icon" href="favicon.ico">
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            background: #FDF2E9;
            margin: 0;
            padding: 2rem;
            text-align: center;
        }}
        .container {{
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(230, 126, 34, 0.1);
            border-top: 5px solid {color};
        }}
        h1 {{ color: {color}; }}
        .timestamp {{ color: #777; font-size: 0.9em; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Bonjour le Monde !</h1>
        <p>Ce site est déployé automatiquement avec GitHub Actions.</p>
        <p class="timestamp">Généré le {date}</p>
        <p>Auteur : {author}</p>
    </div>
</body>
</html>"""

try:
    Path("index.html").write_text(
        HTML_TEMPLATE.format(
            title=CONFIG["title"],
            color=CONFIG["color"],
            author=CONFIG["author"],
            date=datetime.now().strftime("%d/%m/%Y %H:%M")
        ),
        encoding="utf-8"
    )
    sys.exit(0)
except Exception as e:
    print(f"ERREUR: {e}", file=sys.stderr)
    sys.exit(1)

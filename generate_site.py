#!/usr/bin/env python3
"""
Générateur automatique du site DevOps
Version 2.0 - Résiliente aux erreurs
"""
import datetime
import sys
from pathlib import Path

# Configuration
SITE_CONFIG = {
    "title": "Projet DevOps",
    "main_color": "#E67E22",
    "author": "Bernard Thibaut",
    "refresh_interval": 3600  # 1 heure
}

def generate_html(config):
    """Génère le HTML avec template dynamique"""
    try:
        html_template = f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="{config['refresh_interval']}">
    <title>{config['title']}</title>
    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <style>
        body {{
            font-family: 'Segoe UI', system-ui, sans-serif;
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
            box-shadow: 0 2px 10px rgba(233, 119, 34, 0.2);
            border-top: 5px solid {config['main_color']};
        }}
        h1 {{ color: {config['main_color']}; }}
        .timestamp {{ color: #666; font-size: 0.9em; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Bonjour le Monde !</h1>
        <p>Ce site est déployé automatiquement avec GitHub Actions.</p>
        <p class="timestamp">Généré le {datetime.datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}</p>
        <p>Auteur : {config['author']}</p>
    </div>
</body>
</html>'''
        return html_template
    except Exception as e:
        print(f"ERREUR génération HTML : {str(e)}", file=sys.stderr)
        raise

def main():
    try:
        # Génération HTML
        html_content = generate_html(SITE_CONFIG)
        
        # Écriture sécurisée
        output_path = Path("index.html")
        output_path.write_text(html_content, encoding='utf-8')
        print(f"Fichier {output_path} généré avec succès", file=sys.stderr)
        
        # Code de succès
        sys.exit(0)
        
    except Exception as e:
        print(f"ERREUR CRITIQUE : {str(e)}", file=sys.stderr)
        sys.exit(1)  # Code d'erreur pour GitHub Actions

if __name__ == "__main__":
    main()

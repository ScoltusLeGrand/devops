#!/usr/bin/env python3
import datetime

html_template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projet DevOps</title>
    <link rel="icon" href="favicon.ico" type="image/x-icon">
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
            margin: 0 auto;
            padding: 2rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(233, 119, 34, 0.2);
            border-top: 5px solid #E67E22;
        }}
        h1 {{ color: #E67E22; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Bonjour le Monde !</h1>
        <p>Ce site est déployé automatiquement avec GitHub Actions.</p>
        <p>Dernière mise à jour : {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
    </div>
</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html_template)

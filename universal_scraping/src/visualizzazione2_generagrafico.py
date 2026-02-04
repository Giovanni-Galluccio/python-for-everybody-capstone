import sqlite3
import json

# database connection
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# 1. retrive data
cur.execute('SELECT word FROM Whitelist')
whitelist = [row[0] for row in cur.fetchall()]

labels = []
pagine_data = []
parole_data = []

for parola in whitelist:
    cur.execute('''SELECT COUNT(id), SUM(word_count) FROM Pages 
                   WHERE (url LIKE ? OR html LIKE ?) AND word_count > 0''', 
                ('%'+parola+'%', '%'+parola+'%'))
    res = cur.fetchone()
    if res[0] > 0:
        labels.append(parola.capitalize())
        pagine_data.append(res[0])
        parole_data.append(res[1] if res[1] else 0)

conn.close()

# 2. create HTML/JavaScript
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Analisi Civiltà - Wikipedia Scraping</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ font-family: sans-serif; margin: 50px; background: #f4f4f9; }}
        .container {{ background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
        h1 {{ text-align: center; color: #333; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Analisi Documentazione Civiltà</h1>
        <canvas id="myChart"></canvas>
    </div>

    <script>
        const ctx = document.getElementById('myChart').getContext('2d');
        new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: {json.dumps(labels)},
                datasets: [
                    {{
                        label: 'Numero di Pagine (Frammentazione)',
                        data: {json.dumps(pagine_data)},
                        borderColor: 'rgba(54, 162, 235, 1)',
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        yAxisID: 'y',
                        tension: 0.3,
                        fill: true
                    }},
                    {{
                        label: 'Totale Parole (Densità)',
                        data: {json.dumps(parole_data)},
                        borderColor: 'rgba(255, 99, 132, 1)',
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        yAxisID: 'y1',
                        tension: 0.3,
                        fill: true
                    }}
                ]
            }},
            options: {{
                responsive: true,
                scales: {{
                    y: {{
                        type: 'linear',
                        display: true,
                        position: 'left',
                        title: {{ display: true, text: 'Numero di Pagine' }}
                    }},
                    y1: {{
                        type: 'linear',
                        display: true,
                        position: 'right',
                        title: {{ display: true, text: 'Volume di Parole' }},
                        grid: {{ drawOnChartArea: false }}
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""

# 3. write
with open('grafico_storia.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("🚀 File 'grafico_storia.html' generato con successo!")
print("Aprilo con il tuo browser preferito per vedere i risultati.")
import sqlite3
import csv

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('SELECT word FROM Whitelist')
whitelist = [row[0] for row in cur.fetchall()]

# create CSV
with open('dati_grafico.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Civilta', 'Numero_Pagine', 'Totale_Parole']) # Intestazione

    for parola in whitelist:
        cur.execute('''SELECT COUNT(id), SUM(word_count) FROM Pages 
                       WHERE (url LIKE ? OR html LIKE ?) AND word_count IS NOT NULL''', 
                    ('%'+parola+'%', '%'+parola+'%'))
        res = cur.fetchone()
        if res[0] > 0:
            writer.writerow([parola, res[0], res[1] if res[1] else 0])

print("✅ File 'dati_grafico.csv' creato! Aprilo con Excel per creare il tuo grafico.")
conn.close()
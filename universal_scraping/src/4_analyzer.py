import sqlite3
from bs4 import BeautifulSoup

# database connection
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# ---  1: preparation ---
try:
    cur.execute('ALTER TABLE Pages ADD COLUMN word_count INTEGER DEFAULT 0')
    conn.commit()
    print("✅ Colonna 'word_count' pronta.")
except:
    print("ℹ️  La colonna 'word_count' è già presente.")

# --- FASE 2: analysis ---
# we take all the page with HTML saved
cur.execute('SELECT id, html, url FROM Pages WHERE html IS NOT NULL')
pages = cur.fetchall()

print(f"Analisi quantitativa di {len(pages)} pagine in corso...")

count_aggiornati = 0
for p_id, html_data, url in pages:
    
    soup = BeautifulSoup(html_data, "html.parser")
    
    # cleaning: deleting all is not info
    # we delete menu, script, side table and final references
    for element in soup(["script", "style", "nav", "footer", "header", ".reflist", ".navbox"]):
        element.extract()
        
    # get clean text
    testo_pulito = soup.get_text()
    
    # we split the text for single word
    
    elenco_parole = testo_pulito.split()
    numero_parole = len(elenco_parole)
    
    # update database
    cur.execute('UPDATE Pages SET word_count = ? WHERE id = ?', (numero_parole, p_id))
    count_aggiornati += 1
    
    if count_aggiornati % 20 == 0:
        print(f"Pagine elaborate: {count_aggiornati}...")
        conn.commit()

conn.commit()
print(f"\n✅ Analisi completata!")
print(f"Ora ogni pagina ha il suo peso in parole. Totale pagine aggiornate: {count_aggiornati}")

cur.close()
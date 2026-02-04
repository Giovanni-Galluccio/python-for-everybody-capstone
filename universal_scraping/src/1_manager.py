import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# create table
cur.execute('CREATE TABLE IF NOT EXISTS Whitelist (word TEXT UNIQUE)')
cur.execute('CREATE TABLE IF NOT EXISTS Blacklist (word TEXT UNIQUE)')

def mostra_filtri():
    cur.execute('SELECT word FROM Whitelist')
    white = [r[0] for r in cur.fetchall()]
    cur.execute('SELECT word FROM Blacklist')
    black = [r[0] for r in cur.fetchall()]
    print("\n" + "="*30)
    print("STATO ATTUALE DEI FILTRI")
    print("Whitelist (Cerca):", white if white else "VUOTA (Ricerca libera)")
    print("Blacklist (Evita):", black if black else "VUOTA")
    print("="*30)

while True:
    mostra_filtri()
    print("\nCOSA VUOI FARE?")
    print("1) Aggiungi parola chiave (Whitelist)")
    print("2) Aggiungi termine da escludere (Blacklist)")
    print("3) Svuota Whitelist (Rendi ricerca libera)")
    print("4) Svuota Blacklist")
    print("5) Cancella da Whitelist o Blacklist)")
    print("0) Esci e avvia lo spider")
    
    scelta = input("\nInserisci il numero: ")

    if scelta == '1':
        ingressi = input("Inserisci parole chiave divise da virgola: ").lower().strip()
       
        lista_parole = [p.strip() for p in ingressi.split(',')]
        for w in lista_parole:
            if len(w) > 0:
                cur.execute('INSERT OR IGNORE INTO Whitelist (word) VALUES (?)', (w,))
        print(f"Aggiunte {len(lista_parole)} parole alla Whitelist.")

    elif scelta == '2':
        ingressi = input("Inserisci termini da escludere divisi da virgola: ").lower().strip()
        lista_parole = [p.strip() for p in ingressi.split(',')]
        for b in lista_parole:
            if len(b) > 0:
                cur.execute('INSERT OR IGNORE INTO Blacklist (word) VALUES (?)', (b,))
        print(f"Aggiunte {len(lista_parole)} parole alla Blacklist.")
    elif scelta == '3':
        cur.execute('DELETE FROM Whitelist')
    elif scelta == '4':
        cur.execute('DELETE FROM Blacklist')
    elif scelta == '5':
        mostra_filtri()
        tipo = input("Vuoi eliminare da (W)hitelist o (B)lacklist? ").upper()
        parola = input("Quale parola vuoi eliminare? ").lower().strip()
        tabella = "Whitelist" if tipo == "W" else "Blacklist"
        cur.execute(f'DELETE FROM {tabella} WHERE word = ?', (parola,))
        print(f"Rimosso '{parola}' da {tabella}.")    
    elif scelta == '0':
        break
    
    conn.commit()

conn.close()
print("\nConfigurazione salvata. Ora puoi lanciare lo spider!")
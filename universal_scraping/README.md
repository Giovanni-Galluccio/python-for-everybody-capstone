#🌌 Universal web scraping, filtering and simple content analysis in Python

Questo progetto è un esperimento/evoluzione del progetto facente parte del capstone alla fine del percorso 'Python for everybody'(Coursera), sono partito dal progetto originale 'pagerank'.
L'ho realizzato prima del termine del corso per consolidare delle nozioni appena acquisite.

##🎯 Obbiettivo del progetto

Il mio scopo era trasformare qualcosa di già pronto in altro che potessi sentire più 'mio', anche se ovviamente mi mancano ancora le conoscenze per coprire alcune parti. Volevo rendere quello strumenti più universale e più comodo da usare.
Nel mio caso ho usato Wikipedia e trovavo fastidioso il fatto che nello scraping avevo molte pagine 'vuote' e non interessanti per la mia ricerca, come collegamanti ed indici.

In pochi punti:
-più flessibiile
-più controllabile
-più dati puliti

##🤖 Uso dell'inteligenza artificiale (LLM--> Gemini, ChatGPT)

Durante lo sviluppo, pur portando le mie idee al progetto, ho usato l'AI per aiutarmi, esplorando argomenti che giustamente con un corso base non avevo neanche trattato,(la parte della visualizzazione per quanto riguarda il file excel e html sono state interamente fatte da l'AI senza nessun mio contributo).
Comunque decisioni finali e andamento del progetto hanno la mia paternità.

In pochi punti:
-chiarire concetti ancora non consolidati
-esplorare soluzioni alternative
-migliorare la struttura del codice
-comprendere errori e comportamenti inattesi su alcuni siti web

##🚀 Funzionalità principali

###🔷 Sistema filtri dinamici
(Whitelist/Blacklist)
-menu interattivo da terminale
-visualizzazione dei filtri
-possibilità tra:
 -aggiungere parola chiave
 -escludere termini
 -svuotare liste
 -reset filtri
 
###🕷️ Spider avanzato
-User-Agent personalizzato per simulare un browser reale
-integrazione filtri direttamente nella fase di scraping
-parsing mirato a contenuti html


###📊 Analisi testuale
-conteggio parole per singolo link
-analisi quantità testo pagine

###📈 Esportazione e visualizzazione 
Completamente AI(senza un mio intervento)

##🧠 Architettura del progetto

### Ordine di esecuzione consigliata

1_manager.py --> configurazione (whitelist/blacklist)
2_spider.py --> scraping mirato delle pagine
3_rank.py --> ranking delle pagine
4_analyzer --> analisi delle parole
5_visualizzazione1_esportadati.py --> creazione file cvs per excel
6_visualizzazione2_generagrafico.py --> visualizzazione grafica diretta tramite file html

Possono essere eseguiti anche i file originali dopo la parte dello spider per avere una configurazione a nodi.

##🔧 Tecnologie utilizzate
-Python
-Web scraping
-SQLite
-HTML

##📌 Note finali

Questo progetto è stato molto importante perchè mi ha permesso di scoprire quante funzioni possono essere collegate insieme per progettare un sistema completo e funzionale.

A termine ho poi trovato alcune conclusioni, nello specifico io volevo cercare quale civiltà storica fosse la più documentata su Wikipedia, ma la ricerca per parole chiavi mi ha portato a più separazioni, come per esempio Regno/Civiltà/Popolo dividendo di fatto alcuni argomenti appartenenti alla stessa civiltà.
Una possibile soluzione sarebbe stata l'analisi del titolo, magari analizzando tutti i titoli e con la parola più frequente(es. Roma,romani) avrebbe creato un unico blocco. Oppure usare WikiData sfruttando i codici, ancora meglio per i computer, nonostante le possibilità ho preferito fermarmi sia per concludere il corso, una questione di tempo, sia perchè già per la parte di visualizzazione ho dovuto far fare tutto all'AI e non mi piaceva continuare in quel senso, non sarebbe stato più il 'mio' progetto.
### homeworkAlgoritmi2

TRAVELLING SALESMAN PROBLEM:

- Algoritmi Esatti : Held , Karp,  deve terminare in T minuti anche se non trova una soluzione
- Euristiche Costruttive : Nearest Neighbour, Closest Insertion, Farthest Insertion, Random Insertion, Cheapest Insertion. SCEGLIERE UNA
- Algoritmo 2-approssimato: implementate l'algoritmo 2-approssimato basato sull'albero di copertura minimo.

# Gestione dell'input e calcolo corretto delle distanze:
    File in formato GEO: la coordinata x è la latitudine, la coordinata y la longitudine
    convertire le coordinate x,y in radianti usando il codice specificato nelle TSPLIB FAQ (Q: I get wrong distances for problems of type GEO.). La formula considera la parte intera di x e y (NON ARROTONDA ALL'INTERO PIU' VICINO).
    calcolare la distanza geografica tra i punti i e j usando il codice presente nelle FAQ per "dij". Anche in questo caso il codice considera la parte intera delle distanze.

    File in formato EUC_2D: In questo caso non occorre fare conversioni di coordinate. Calcolare la distanza Eculidea e arrotondate il valore all'intero più vicino.

# Cosa consegnare
Una breve relazione sullo svolgimento del progetto. La relazione deve contenere:
una sezione introduttiva con la descrizione degli algoritmi e delle scelte implementative che avete fatto;
tabella esplicativa dei risultati e le risposte alle due domande;
eventuali originalità introdotte nell'elaborato o nell'implementazione;
una sezione conclusiva in cui porre i vostri commenti e le vostre conclusioni sull’elaborato svolto e i risultati ottenuti.
Il codice sorgente dell’implementazione in un unico file di archivio (.zip, .tar.gz, ecc.).
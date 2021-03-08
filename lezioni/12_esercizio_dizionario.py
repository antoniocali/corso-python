text = "ciao mi chiamo antonio e questo e' un testo un po' lungo ma anche un po' corto cosi' giusto per dire"

dizionario_lettere = {}
for parola in text.split():
    prima_lettera = parola[0]
    if prima_lettera not in dizionario_lettere:
        dizionario_lettere[prima_lettera] = [parola]
    else:
        temp_list = dizionario_lettere[prima_lettera]
        temp_list.append(parola)
        dizionario_lettere[prima_lettera] = temp_list

print(dizionario_lettere)

# Esercizio 1
# Funzione che dato un testo mi restituisce il dizionario in cui per ogni lunghezza mi dice le parole di quella lunghezza
# Esempio: ciao sono antonio -> {4: [ciao, sono], 7: [antonio]}
# Esercizio 2
# Funzione che dato un testo mi restitusce quali lettere e in che quantita' sono presenti all'interno del testo
# Esempio: ciao sono -> {c:1, i:1, a:1, o:3, s:1, n:1}
# Esercizio 3
# Funzione che dato un testo, mi restitusca per ogni parole, le sue lettere e in quale quantita'
# esempio: ciao sono ciao -> {ciao: {c:2,i:2,a:2,o:2}, sono: {s:1,o:2,n:1}}

# Esercizio 4
# Riprendete la lista della spesa, ma aggiornate il codice, in modo che vi sia una nuova funzione che permetta di aggiornare
# La quantita' di un prodotto


# creare una variabile con un testo lungo a piacere
text = "ciao mi chiamo antonio come va, ciao mi chiamo antonio antonio antonio lettera"
word = "antonio"


# creare una funzione che accetta un parametro di tipo stringa, una parola
# voglio spaere quante volte quella parola appare nel testo
# hint: utilizzare la funzione split sulle stringhe

def count_parola(testo: str, parola: str, sep: str = " "):
    _lista = testo.replace(",", "").split(sep=sep)
    contatore = 0
    for elemento in _lista:
        if elemento == parola:
            contatore = contatore + 1
    return contatore


pippo = count_parola(testo=text, sep=' ', parola=word)
print(f"Nel testo {text} la parola {word} appare {pippo} volte")


# seconda funzione che chiamo max_length, senza parametri
# mi restituisce la parola piu' lunga del testo e la sua lunghezza

def max_length(testo: str):
    _lista = testo.split()
    lunghezza_massima_attuale = -1
    lista_di_parole = []
    for elemento in _lista:
        if len(elemento) > lunghezza_massima_attuale:
            lunghezza_massima_attuale = len(elemento)
            lista_di_parole = [elemento]
        elif len(elemento) == lunghezza_massima_attuale and elemento not in lista_di_parole:
            lista_di_parole.append(elemento)

    return (lunghezza_massima_attuale, lista_di_parole)

prova = max_length(testo=text)
print(f"Nel testo {text}, la parola piu' lunga e' {prova[1]} con la sua lunghezza di {prova[0]} caratteri")


print(count_parola("antonio!pippo!pippo!antonio","antonio"))


# Esercizio 1
# creare una funzione che rimuova i duplicati da una lista
# Ovvero sempio funzione([1,1,1,2,3,3,4,5,2]) ==> [1,2,3,4,5]

# Esercizio 2
# Scrivere una funzione che rimuova i numeri pari da una lista
# esempio: f([1,2,3,4,5]) ==> [1,3,5]

# Esercizio 3
# Scrivere una funzione che rimuova gli elementi che stanno in posizioni pari di una lista
# esempio: f([1,2,3,4,5]) ==> [2,4]

# Esercizio 4
# FizzBuzz, ovvero una funzione che accetti una lista di numeri e per ogni elemento della lista:
# se l'elemento e' multiplo di 3 print Fizz
# se l'elemento e' multiplo di 5 print Buzz
# se l'elemento e' contemporaneamente multiplo sia di 3 che di 5 (es, 15) scrivere FizzBuzz







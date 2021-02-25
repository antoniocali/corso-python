# Esercizio 1
# creare una funzione che rimuova i duplicati da una lista
# Ovvero sempio funzione([1,1,1,2,3,3,4,5,2]) ==> [1,2,3,4,5]
from typing import List, Tuple


def rimuovi_duplicati(lista: List) -> List:
    _lista = []
    for elem in lista:
        if elem not in _lista:
            _lista.append(elem)

    return _lista


print(rimuovi_duplicati([1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 1]))


# Esercizio 2
# Scrivere una funzione che rimuova i numeri pari da una lista
# esempio: f([1,2,3,4,5]) ==> [1,3,5]

def rimuovi_pari(lista: List) -> List:
    _lista = []
    for elem in lista:
        if elem % 2 != 0:
            _lista.append(elem)
    return _lista


print(rimuovi_pari([0, 1, 2, 3, 4, 5, 6, 7]))


# Esercizio 3
# Scrivere una funzione che rimuova gli elementi che stanno in posizioni pari di una lista
# esempio: f([1,2,3,4,5]) ==> [2,4]

def rimuovi_posizioni_pari(lista: List) -> List:
    _lista = []
    for indice, elem in enumerate(lista):
        if indice % 2 != 0:
            _lista.append(elem)
    return _lista


print(rimuovi_posizioni_pari([1, 2, 3, 4, 5, 6, 7]))


# Esercizio 4
# FizzBuzz, ovvero una funzione che accetti una lista di numeri e per ogni elemento della lista:
# se l'elemento e' multiplo di 3 print Fizz
# se l'elemento e' multiplo di 5 print Buzz
# se l'elemento e' contemporaneamente multiplo sia di 3 che di 5 (es, 15) scrivere FizzBuzz

def fizzbuzz(lista: List):
    for elem in lista:
        if elem % 3 == 0 and elem % 5 != 0:
            print("Fizz")
        elif elem % 5 == 0 and elem % 3 != 0:
            print("Buzz")
        elif elem % 5 == 0 and elem % 3 == 0:
            print("FizzBuzz")
        else:
            print(elem)


# fizzbuzz([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])


def fizzbuzz_v2(lista: List) -> List:
    _lista = []
    for elem in lista:
        if elem % 3 == 0 and elem % 5 != 0:
            _lista.append("fizz")
        elif elem % 5 == 0 and elem % 3 != 0:
            _lista.append("buzz")
        elif elem % 5 == 0 and elem % 3 == 0:
            _lista.append("fizzbuzz")
        else:
            _lista.append(str(elem))
    return _lista


print(fizzbuzz_v2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))


# Esercizio 5:
# Funzione che accetta due liste. Iterate su entrambe le liste per creare le coppie di elementi: esempio [1,2,3,4] [a,b,c,d] -> [(1,a),(2,b),(3,c),(4,d)]

def crea_coppia(lista1: List, lista2: List) -> List:
    _lista = []
    indice = 0
    if len(lista1) != len(lista2):
        return []
    while indice < len(lista1):
        tmp_tupla = (lista1[indice], lista2[indice])
        _lista.append(tmp_tupla)
        indice = indice + 1
    return _lista


def crea_coppia_2(lista1: List, lista2: List) -> List:
    _lista = []
    if len(lista1) != len(lista2):
        return []
    for indice, elem in enumerate(lista1):
        tmp_tupla = (elem, lista2[indice])
        _lista.append(tmp_tupla)
    return _lista


def crea_coppia_3(lista1: List, lista2: List, lista3: List) -> List:
    return list(zip(lista1, lista2, lista3))  # int("10"), float("5.0"), str(4), list(zip)


print(crea_coppia([1, 2, 3, 4], ["a", "b", "c"]))
print(crea_coppia_2([1, 2, 3], ["a", "b", "c"]))
print(crea_coppia_3([1, 2, 3, 4, 5], ["a", "b", "c"], [False, True, True]))


# Esercizio 6:
# Funzione che accetta una stringa, e mi restituisce la stringa a parole inverse: esempio "Ciao mi chiamo Antonio" -> "Antonio chiamo mi Ciao"

# [1,2,3]
def inverti_lista(lista: List) -> List:
    _lista = []
    for indice, _ in enumerate(lista):
        tmp_indice = len(lista) - indice - 1  # 3 - 0 - 1 = 2
        _lista.append(lista[tmp_indice])
    return _lista


#   0        1        2        3        4      (lunghezza = 5)
# 5-0-1=4  5-1-1=3  5-2-1=2  5-3-1=1  5-4-1=0

print(inverti_lista([1, 2, 3]))


def inverti_stringa(testo: str) -> str:
    _list = testo.split()
    _lista_inverita = inverti_lista(_list)
    _stringa = ""
    for elem in _lista_inverita:
        _stringa = _stringa + elem + " "
    return _stringa


def inverti_stringa_2(testo: str) -> str:
    _list = testo.split()
    _list.reverse()
    _stringa = ""
    for elem in _list:
        _stringa = _stringa + elem + " "
    return _stringa


def inverti_stringa_3(testo: str) -> str:
    _list = testo.split()
    _list.reverse()
    _stringa = " ".join(_list)
    return _stringa


print("ciao".upper())
print(":".join(["1", "2", "3", "4"]))
print("+".join(["1", "2", "3", "4"]))
print("ciaomichiamoantonio".join(["1", "2", "3", "4"]))

lista = [1, 2, 3, 4]
print(f"{lista=}")
lista.reverse()
print(f"{lista=}")
print(f"{inverti_stringa('Ciao mi chiamo Antonio')=}")
print(f"{inverti_stringa_2('Ciao mi chiamo Antonio')=}")
print(f"{inverti_stringa_3('Ciao mi chiamo Antonio')=}")


# Esercizio 3:
# Funzione che accetta una lista di interi e un intero, restiuisce una lista tre lliste, quella degli elementi minori dell'intero, la lista del numero stesso, lista dei numeri maggiori dell'intero. Esempio ([3,1,6,3,7,6,5,9,10,0,2], 6) -> [3,1,3,5,0,2],[6,6],[7,9,10]
def genera_liste(lista: List, numero: int) -> Tuple:
    minore = []
    uguale = []
    maggiore = []
    for elem in lista:
        if elem < numero:
            minore.append(elem)
        elif elem == numero:
            uguale.append(elem)
        else:
            maggiore.append(elem)
    return (minore, uguale, maggiore)


print(genera_liste([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))


# Esercizio 4:
# Creare una funzione che accetti 3 interi, inizio, fine, passo. Genera una lista di numeri che partano da inizio, fino a fine, saltando di passo in passo. Esempio, inizio=3, fine=9, passo=2 -> [3,5,7,9]
# Esercizio 4-Bonus => Rendere passo un parametro opzionale, di default = 1

def genera_numeri(start: int, end: int, step: int = 1) -> List:
    lista = []
    while start < end:
        lista.append(start)
        start = start + step
    return lista


print(f"{genera_numeri(start=1,end=10,step=2)=}")
print(f"{genera_numeri(start=1,end=10,step=1)=}")
print(f"{genera_numeri(start=1,end=10,step=4)=}")

print(fizzbuzz_v2(genera_numeri(1, 1000)))
print(inverti_lista(genera_numeri(1, 10)))

print(list(range(1, 10, 1)))

# enumerate object che non e' una lista
print(enumerate([1, 2, 3]))
# zip object che non e' una lista
print(zip([1, 2, 3], [2, 3, 4]))

# ma possiamo far for-loop su enumerate objects
for indice, elem in enumerate([1, 2, 3]):
    print(indice, elem)

# possiamo fare for-loop su zip objects
for elem1, elem2 in zip([1, 2, 3], ["a", "b", "c"]):
    print(elem1, elem2)

# possiamo fare for-loop su range objects
for elem in range(1, 4):
    print(elem)


# 1. funzione che accetta due liste, che ritorni, una lista con gli elemnti comuni ad entrambe le liste:
# esempio [1,2,4,5,6,7], [2,5,1,9,10] -> [2,5,1] (in qualsiasi ordine)

# 2. funzione che accetta due liste, ritorni un booleano che indica se la seconda lista e' una sottolista della prima
# esempio [1,2,3,4,5,6,7], [3,4,5] -> True
# esempio 2 [1,2,3,4,5], [3,5] -> False

# 3. funzione che acceta due liste, ritorni una lista con i valori mancanti della seconda rispetto alla prima
# esempio 1> [1,2,3,4,5], [2,4,6] -> [1,3,5]

# 4. funzione che accetta una stringa, ritorni quale lettera appare di piu' all'interno della stringa
# esempio "ciao sono antonio" -> (o, 5)
# cercate su google come iterare sulle stringhe!



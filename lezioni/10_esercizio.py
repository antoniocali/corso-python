# 1. funzione che accetta due liste, che ritorni, una lista con gli elemnti comuni ad entrambe le liste:
# esempio [1,2,4,5,6,7], [2,5,1,9,10] -> [2,5,1] (in qualsiasi ordine)
from typing import List, Tuple

lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [2, 3, 4, 7, 8]
lista_c = lista_a + [1, 5]
lista_d = [1, 5]


def intersezione(lista1: List[int], lista2: List[int]) -> List[int]:
    _lista: List[int] = []
    for elem in lista1:
        if elem in lista2:
            _lista.append(elem)
    return _lista


print(intersezione(lista_a, [2, 4, 5]))


# 2. funzione che accetta due liste, ritorni un booleano che indica se la seconda lista e' una sottolista della prima
# esempio [1,2,3,4,5,6,7], [3,4,5] -> True
# esempio 2 [1,2,3,4,5], [3,5] -> False

def sottolista(lista: List[int], sublist: List[int]) -> bool:
    index = 0
    lunghezza_lista = len(lista)
    lunghezza_sub = len(sublist)
    print(lista, sublist)
    while index < lunghezza_lista:
        sub_index = 0
        to_continue = True
        while sub_index < lunghezza_sub and to_continue and index + sub_index < lunghezza_lista:
            if sublist[sub_index] != lista[index + sub_index]:
                to_continue = False
            sub_index = sub_index + 1
        if sub_index == lunghezza_sub:
            return True
        index = index + 1
    return False

def sottolista2(lista: List[int], sublist: List[int]) -> bool:
    print(lista, sublist)
    start = 0 # indice che mi serve ad avanzare nella lista generale
    index = 0 # indice che mi permette di confrontare la sottolista (che sara' sempre a elementi 0,1,2) con la lista principale (che avanza con start)
    while start + index < len(lista):
        print(f"{start=}, {index=}")
        if lista[start + index] != sublist[index]:
            start = start + index
            index = 0
        elif index == len(sublist)-1:
            return True
        else:
            index = index + 1
    return False
print(sottolista2([1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,7],[1,2,3,4,5,6,7]))

# 3. funzione che acceta due liste, ritorni una lista con i valori mancanti della seconda rispetto alla prima
# esempio 1> [1,2,3,4,5], [2,4,6] -> [1,3,5]

def minus(lista1: List[int], lista2: List[int]) -> List[int]:
    _lista: List[int] = []
    for elem in lista1:
        if elem not in lista2:
            _lista.append(elem)
    return _lista


print(minus(lista_a, lista_b))

# 4. funzione che accetta una stringa, ritorni quale lettera appare di piu' all'interno della stringa
# esempio "ciao sono antonio" -> (o, 5)
# cercate su google come iterare sulle stringhe!

def conta_lettera(text: str, lettera: str) -> int:
    _count = 0
    for _lettera in text:
        if lettera == _lettera:
            _count = _count + 1
    return _count

def lettera(text: str) -> Tuple[int, str]:
    _lista_visti: List[str] = []
    max_lettera = ""
    max_count = -1
    for _lettera in text:
        if _lettera not in _lista_visti:
            count = conta_lettera(text=text, lettera=_lettera)
            if count > max_count:
                max_count = count
                max_lettera = _lettera
            _lista_visti.append(_lettera)
    return (max_count, max_lettera)


print(lettera("ciao mi chiamo antonio questo e' il mio nome iiiiiiiii"))
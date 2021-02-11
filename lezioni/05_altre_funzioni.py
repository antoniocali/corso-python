lezione_numero = 5
print(f"Lezione {lezione_numero}")


# print(3 / 2)
# print(7 % 2)


def somma_piu_uno(a, b):
    return a + b


# somma = somma_piu_uno(3,4)
# print("Secondo print " + str(somma))

def e_pari(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def modulo(numero, mod):
    print(f"{numero} % {mod} = {numero % mod}")


pari_4 = e_pari(4)


# modulo(5,4)
# modulo(5,5)
# print(5**2)
# print(2.0**(1/2))

# import math
# print(math.pi)
# print(math.pow(2,2))

# from math import cos, sin
# print(cos(0))
# print(sin(0))
# print()
# stringa = "TUTTO IN MAIUSCOLO"
# stringa2 = "tUTTo in minuscolo"
# print(stringa)
# print(stringa.lower())
# print(stringa2)
# print(stringa2.upper())
# print("Questa Stringa Sara' in minuscolo".lower())
# print("questa stringa sara' maiuscola".upper())
# print(1.0)
# print("metodi e funZione".capitalize())
# print("cosa posso chiedere".startswith("cosa"))
# print("altro?".endswith("?"))
# print("1".upper())
# print(1.0)
# print(type("stringa"))
# print(type(1))
# print(type(1.0))
# print(type(False))

# 1- Crea una funzione chiamata cerca_parola che abbia due parametri entrambi stringhe:
#   il primo parametro e' una stringa a piacere, il secondo invece una parola che vogliamo sapere essere presente
#   nella prima stringa
#   La funzione deve restiture True se la parola e' presente nella stringa, altrimenti False
#   str.find() "ciao mi chiamo antonio".find()

# 2 - Copia incolla dell'uno, ma con un terzo parametro che e' un booleano che chiama CaseSensitive.
#    se il terzo parametro e' True: allora nella ricerca della parola dobbiamo essere casesensitive (ovvero se cerco Antonio o antonio da' un risultato diverso)
#    se invece e' false non e' case sensitve, e allora cercare AntoNio e aNTonio e' la stessa cosa


def cerca_parola(testo: str, parola_da_cercare: str):
    print("I valori di cerca_parola sono:")
    print(f"{testo=}")
    print(f"{parola_da_cercare=}")
    parola_trovata = testo.find(parola_da_cercare)
    if parola_trovata == -1:
        return False
    else:
        return True


def cerca_parola_2(testo2: str, parola2: str, case_sentive: bool):
    print("I valori di cerca_parola_2 sono:")
    print(f"{testo2=}")
    print(f"{parola2=}")
    print(f"{case_sentive=}")
    if case_sentive:
        parola_trovata = cerca_parola(testo2, parola2)
        return parola_trovata
    else:
        testo_uppercase = testo2.upper()
        parola2_uppercase = parola2.upper()
        parola_trovata = cerca_parola(testo_uppercase, parola2_uppercase)
        return parola_trovata


print(f"parola trovata? {cerca_parola_2('mi chiamo antonio', 'AnTOnio', True)}")


def funzione_2(param1, param2):
    print(f"{param1=} {param2=}")


funzione_2("testo", 3)


def funzione_3(param1: str, param2: bool):
    print(f"{param1=} {param2=}")


funzione_3("testo", True)

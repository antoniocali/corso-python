# print(int("a"))
# print(5/0)

# try:
#     print("Generazione di errore")
#     int("a")
#     divisione = 5/0
#     print("Dopo l'errore, questo non viene stampato")
# except ValueError as exception:
#     print(f"L'eccezione generata e': {exception}")
# except ZeroDivisionError as exception:
#     print(exception)


def menu():
    print("Scegli tra")
    print("1")
    print("2")
    print("3 - fine programma")
    try:
        scelta_utente = int(input(""))
    except:
        print("Hai inserito un testo che non e' un numero")
        scelta_utente = -1
    return scelta_utente

scelta_utente = menu()
while scelta_utente != 3:
    if scelta_utente == 1:
        print("Ecco")
    elif scelta_utente == 2:
        print("Oh la")
    else:
        print("Numero non riconosciuto")
    scelta_utente = menu()

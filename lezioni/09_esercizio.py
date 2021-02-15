# lista iniziale vuota
# creaimo il nostro menu
# Il nostro menu ci mette a disposizione diverse funzioni
# 1. Aggiungi spesa: Funzione che chiede all'utente quanto equivale la spesa e aggiunge la spesa come valore negativo alla nostra
# lista iniziale vuota
# 2. Aggiungi Entrate: Funzione che utente quanto, e aggiunge il valore come positivo alla nostra lista
# 3. Spesa totale: funzione che ci dice quante spese abbiamo fatto (for sulla lista)
# 4. saldo: Funzione che ci dice quanto e' il nostro attuale bilancio
# 5. Inventario: Funzione che ci stampa a scheermo tutte le nostre spese e entrate in ordine di come sono state inserite

inventario = []


def aggiungi_importo(messaggio_utente: str, is_spesa: bool):
    try:
        importo = float(input(messaggio_utente))
    except ValueError:
        print("Hai inserito un importo non valido")
    else:
        if importo >= 0 and is_spesa:
            importo = -importo
        elif importo < 0 and is_spesa == False:
            importo = -importo

        inventario.append(importo)


def aggiungi_spesa():
    try:
        spesa = float(input("Inserisci quanto hai speso"))
    except ValueError:
        print("Hai inserito un importo non valido")
    else:
        if (spesa >= 0):
            inventario.append(-spesa)
        else:
            inventario.append(spesa)
        print(f"Hai aggiunto {spesa}")


def aggiungi_entrata():
    try:
        spesa = float(input("Inserisci la tua entrata"))
    except ValueError:
        print("Hai inserito un importo non valido")
    else:
        if (spesa >= 0):
            inventario.append(spesa)
        else:
            inventario.append(-spesa)
        print(f"Hai aggiunto {spesa}")


def spese_totali():
    valore_iniziale = 0
    for elemento in inventario:
        if elemento < 0:
            valore_iniziale = valore_iniziale + elemento
    return valore_iniziale


def saldo():
    return sum(inventario)


def stampa_inventario():
    for indice, elemento in enumerate(inventario):
        print(f"{indice + 1}) {elemento}")


def menu():
    print("Scegli")
    print("1 - inserisci spesa")
    print("2 - inserisci entrata")
    print("3 - spese totali")
    print("4 - saldo")
    print("5 - inventario")
    print("6 - chiudi")


menu()


def scelta():
    try:
        return int(input(""))
    except ValueError:
        return -1


scelta_utente = scelta()
while scelta_utente != 6:
    if scelta_utente == 1:
        aggiungi_importo("Quanto hai speso", True)
    elif scelta_utente == 2:
        aggiungi_importo("Quanto hai guadagnato", False)
    elif scelta_utente == 3:
        spesa = spese_totali()
        print(f"Hai speso {-spesa}")
    elif scelta_utente == 4:
        print(f"Il tuo saldo e' {saldo()}")
    elif scelta_utente == 5:
        stampa_inventario()
    else:
        print("Hai inserito un valore non valido")
    menu()
    scelta_utente = scelta()

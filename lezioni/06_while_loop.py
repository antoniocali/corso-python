print("Lezione 6 - While Loop")

ho_contato_fino_a = 6

while ho_contato_fino_a <= 5:
    print(f"Sto aspettando.. Ho contato fino a {ho_contato_fino_a}")


# print("Ti mando a quel paese")

def stampa_menu():
    print("Scegli:")
    print("1 - Di ciao")
    print("2 - Di arriverci")
    print("3 - Fine programma")

stampa_menu()

scelta_utente = int(input("Scegli cosa vuoi fare attraverso un numero"))

while scelta_utente != 3:
    if scelta_utente == 1:
        print("Ciao")
    elif scelta_utente == 2:
        print("Arrivederci")
    else:
        print("comando non riconosciuto")
    stampa_menu()
    scelta_utente = int(input("Scegli cosa vuoi fare attraverso un numero"))


# Creare un Menu
# Il programma continua fintanto che l'utente non sceglie il valore 3
# Con 3 scelte:
# Scelta 1 - Perimetro Triangolo (lati chiesti all'utente)
# Scelta 2 - Area Triangolo (altezza e base chiesti all'utente)
# Scelta 3 - Fine programma
# Altri numeri => Numero non riconosciuto. Riparte

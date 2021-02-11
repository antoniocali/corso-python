# Creare un Menu
# Il programma continua fintanto che l'utente non sceglie il valore 3
# Con 3 scelte:
# Scelta 1 - Perimetro Triangolo (lati chiesti all'utente)
# Scelta 2 - Area Triangolo (altezza e base chiesti all'utente)
# Scelta 3 - Fine programma
# Altri numeri => Numero non riconosciuto. Riparte

def perimetro():
    lato1 = int(input("lato1"))
    lato2 = int(input("lato2"))
    lato3 = int(input("lato3"))
    if lato1 > 0 and lato2 > 0 and lato3 > 0:
        print(f"Il perimetro di lati {(lato1, lato2, lato3)} e' {lato1+lato2+lato3}")
    else:
        print("Triangolo non valido")

def area():
    altezza = int(input("altezza"))
    base = int(input("base"))
    if altezza > 0 and base > 0:
        print(f"L'area del triangolo di {base=} e {altezza=} e' {(base*altezza)/2}")
    else:
        print("Triangolo non valido")

def menu():
    print("Scegli fra")
    print("1 - Perimetro")
    print("2 - Area")
    print("3 - Fine programma")
    scelta_utente = int(input(""))
    return scelta_utente

scelta_utente = menu()
while scelta_utente != 3:
    if scelta_utente == 1:
        perimetro()
    elif scelta_utente == 2:
        area()
    else:
        print("Numero non riconosciuto")
    scelta_utente = menu()


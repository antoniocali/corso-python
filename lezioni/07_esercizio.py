# Creare un Menu
# Il programma continua fintanto che l'utente non sceglie il valore 3
# Con 3 scelte:
# Scelta 1 - Perimetro Triangolo (lati chiesti all'utente)
# Scelta 2 - Area Triangolo (altezza e base chiesti all'utente)
# Scelta 3 - Fine programma
# Altri numeri => Numero non riconosciuto. Riparte
# Gestire errori per cui: Utente non mette dei numeri ma testi => Informare l'utente di quel che ha fatto e pentirsene!
# Generare un ValueError se Utente mette lati negativi => Utente Beota, allora giustamente generiamo errori
# Gestire Errore per cui Utente ha messo lati negativi. => Ma siamo clementi, e li catturiamo e informiamo l'utente di quel che ha fatto
x = True
def perimetro():
    try:
        lato1 = int(input("Lato1"))
        lato2 = int(input("Lato2"))
        lato3 = int(input("Lato3"))
        if lato1 > 0 and lato2 > 0 and lato3 > 0:
            print(f"perimetro = {lato1 + lato2 + lato3}")
        else:
            raise ValueError("Hai messo un lato negativo")
    except ValueError as e:
        print(f"Errore: {e}")

def area():
    try:
        base = float(input("base"))
        if base < 0:
            raise ValueError("Base negativa")
        altezza = float(input("altezza"))
        if altezza < 0:
            raise ValueError("Altezza negativa")
        print(f"area {(base*altezza)/2}")
    except ValueError as e:
        print(f"Errore: {e}")

def menu():
    print("Scegli")
    print("1")
    print("2")
    print("3")
    try:
        scelta = int(input(""))
    except ValueError as e:
        scelta = -1
    finally:
        return scelta

while x:
    scelta_utente = menu()
    if scelta_utente == 1:
        perimetro()
    elif scelta_utente == 2:
        area()
    elif scelta_utente == 3:
        x = False
    else:
        print("Errore")



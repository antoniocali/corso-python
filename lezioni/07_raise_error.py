
def menu():
    print("Scegli")
    print("1")
    print("2")
    print("3 - Fine Programma")
    try:
        scelta_utente = int(input(""))
    except:
        scelta_utente = -1
    finally:
        print(f"E' stato scelto {scelta_utente}")
        return scelta_utente

scelta_utente = menu()
while scelta_utente != 3:
    if scelta_utente == 1:
        print("Hello")
    elif scelta_utente == 2:
        print("Goodbye")
    else:
        # print("Numero non riconosciuto")
        try:
            raise ValueError(f"Hai inserito {scelta_utente}. Numero non riconosciuto")
        except ValueError as e:
            print(f"Eheh scherzone. {e}")
    scelta_utente = menu()


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

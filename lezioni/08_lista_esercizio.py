# una funzione chiamata calcolo_perimetro_n.
# Nessun parametro
# creiamo una lista vuota
# chiediamo all'utente di inserire il lato i-esimo del nostro poligono
# fintanto che l'utente inserisce lati positivi, aggiungiamo il lato alla lista
# se l'utente mette -1, esso indica la fine del nostro while per aggiungere lati
# infine, andiamo a calcolare il perimetro del poligono
# di lati aggiunti dall'utente attraverso un nuovo while sulla lista
# che abbiamo generato con i valori dell'utente

def calcolo_perimetro_n():
    lista_lati = []
    try:
        lato_temporaneo = int(input("Inserisci lato"))
        while lato_temporaneo != -1:
            if lato_temporaneo > 0:
                lista_lati.append(lato_temporaneo)
            else:
                print("Hai inserito un lato negativo")
            lato_temporaneo = int(input("Insersci lato"))
    except ValueError as e:
        print("Hai inserito un valore errato")
    else:
        index = 0
        somma_perimetro = 0
        while index < len(lista_lati):
            somma_perimetro = somma_perimetro + lista_lati[index]
            index = index + 1

        print(f"Hai inserito i lati {lista_lati} e il perimetro del poligono di {len(lista_lati)} lati e' uguale a {somma_perimetro}")

calcolo_perimetro_n()
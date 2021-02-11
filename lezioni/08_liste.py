print("Lezione 8")

persone = ["antonio", "pippo", "davide", "giulia"]
numeri = [0, 1, 2, 3, 4]
booleani = [False, True, True, False, False]
lista_vuota = []

print(persone)
print(persone[0])
print(persone[1])
print(persone[2])
print(persone[3])
print(f"persone ha lunghezza: {len(persone)}")
print(len("antonio ,"))

persone.append("marco")
print(persone)
print(f"persone ha lunghezza: {len(persone)}")
elemento_rimosso = persone.pop(0)
print(elemento_rimosso)
print(persone)
persone.remove("giulia")
print(persone)
liste_miste = ["stringa", 1, False, 2.0]
print("paperino" in persone)

index = 0
lunghezza_lista = len(persone)
print(f"{lunghezza_lista=}")
while index < lunghezza_lista:
    print(f"{index}. {persone[index]}")
    index = index + 1

print(numeri)
index = 0
while index < len(numeri):
    elemento = numeri[index]
    if elemento % 2 == 0:
        print(f"{elemento} e' pari")
    else:
        print(f"{elemento} e' dispari")
    index = index + 1

# una funzione chiamata calcolo_perimetro_n.
# Nessun parametro
# creiamo una lista vuota
# chiediamo all'utente di inserire il lato i-esimo del nostro poligono
# fintanto che l'utente inserisce lati positivi, aggiungiamo il lato alla lista
# se l'utente mette -1, esso indica la fine del nostro while per aggiungere lati
# infine, andiamo a calcolare il perimetro del poligono
# di lati aggiunti dall'utente attraverso un nuovo while sulla lista
# che abbiamo generato con i valori dell'utente


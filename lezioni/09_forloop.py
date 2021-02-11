print("Lezione 9")

lista_temporanea = ["a", "b", "c", "d"]
#
# index = 0
# while index < len(lista_temporanea):
#     oggetto_temporaneo_della_lista = lista_temporanea[index]
#     print(f"{index}) {oggetto_temporaneo_della_lista}")
#     index = index + 1

# for-loop
# ["a", "b", "c", "d"] -> enumerate(["a", "b", "c", "d"]) -> [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
for oggetto_temporaneo in enumerate(lista_temporanea):
    print(f"{oggetto_temporaneo[0]}) {oggetto_temporaneo[1]}")

# liste
mia_lista = [1, 2, 3, 4]
mia_lista.append(5) # aggiungi elemento
mia_lista.pop() #rimuovi elemento attraverso l'indice
mia_lista.remove(2) #rimuovi elemento attraverso l'oggetto contentuo
mia_lista[0]  # accede a elemento ad indice 0

# tuple -> Liste non modificabili
mia_tupla = (0, 'a')
indice, valore = mia_tupla


# lista di tuple
# lista_tuple = [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
# for elem in lista_tuple:
#     print(elem)

nuovo_valore = 'a'
nuovo_indice = 0
nuova_tupla = (nuovo_indice, nuovo_valore)
print(f"{nuova_tupla=}")

# lista iniziale vuota
# creaimo il nostro menu
# Il nostro menu ci mette a disposizione diverse funzioni
# 1. Aggiungi spesa: Funzione che chiede all'utente quanto equivale la spesa e aggiunge la spesa come valore negativo alla nostra
# lista iniziale vuota
# 2. Aggiungi Entrate: Funzione che utente quanto, e aggiunge il valore come positivo alla nostra lista
# 3. Spesa totale: funzione che ci dice quante spese abbiamo fatto (for sulla lista)
# 4. saldo: Funzione che ci dice quanto e' il nostro attuale bilancio
# 5. Inventario: Funzione che ci stampa a scheermo tutte le nostre spese e entrate in ordine di come sono state inserite






print("Lezione 12, Dizionari")

liste = [1, 2, 3]
tuple = (1, 2, 3)
dizionari = {
    "ciao": "saluto",
    "sole": "stella principale della via lattea",
    "luna": "Satellite della terra"
}

print(liste[0]) # attraverso la posizione
print(dizionari["ciao"]) #attraverso la chiave
print(dizionari["sole"]) #attraverso la chiave
print(dizionari["luna"]) #attraverso la chiave

print("ciao" in dizionari) # controllo se la chiave e' presente nel dizionario
print(0 in liste) #controllo se l'elemento e' presente nella lista

# Esercizio
# Funzione che accetta una lista e un numero, mi divide la lista in sottoliste grandi quanto quel numero
# Esempio: [1,2,3,4,5,6,7,8,9,10], 2 -> [1,2], [3,4], [5,6], [7,8], [9,10]
# Esempio 2: [1,2,3,4,5], 3 -> [1,2,3],[4,5]
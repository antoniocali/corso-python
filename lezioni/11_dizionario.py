print("Lezione 12, Dizionari")

liste = [1, 2, 3]
tuple = (1, 2, 3)
dizionari = {
    "ciao": "saluto",
    "sole": "stella principale della via lattea",
    "luna": "Satellite della terra"
}

print(liste[0])  # attraverso la posizione
print(dizionari["ciao"])  # attraverso la chiave
print(dizionari["sole"])  # attraverso la chiave
print(dizionari["luna"])  # attraverso la chiave

print("ciao" in dizionari)  # controllo se la chiave e' presente nel dizionario
print(0 in liste)  # controllo se l'elemento e' presente nella lista

# Lunghezza del dizionario?
print(len(dizionari))

# Aggiornare il valore di una chiave
print(dizionari["sole"])  # attraverso la chiave
print("Aggiorniamo valore di sole")
dizionari["sole"] = "nuovo valore"
print(dizionari["sole"])  # attraverso la chiave

# Eliminare invece una chiave il suo valore
print(dizionari)
del (dizionari["luna"])
print(dizionari)

# Iterare sui dizionari
for elemento in dizionari:
    print(f"{elemento}={dizionari[elemento]}")

print("chiave valore attraverso items")
for key, value in dizionari.items():
    print(key, value)

print("solo chiavi")
for valore in dizionari.values():
    print(valore)
print("solo valori")
for key in dizionari.keys():
    print(key)

print(list(dizionari.values()))
print(list(dizionari.keys()))
print(list(dizionari.items()))

dizionari["nuova_chiave"] = "qualcosa"
print(dizionari)

dizionari.update()
if "pippo" in dizionari:
    print(dizionari["pippo"])
else:
    print("valore default")


def dammi_qualcosa(key: str):
    try:
        return dizionari[key]
    except KeyError:
        return "default"


def dammi_qualcosa2(key: str):
    if key in dizionari:
        return dizionari[key]
    else:
        return "default"


def dammi_qualcosa3(key: str):
    return dizionari.get(key, "default")


print(dammi_qualcosa("pippo"))
print(dammi_qualcosa("sole"))
print(dammi_qualcosa3("sole"))

dizionario2 = {
    1: "pippo",
    2: "ello",
    3: "asdfafs"
}
print(dizionario2)
dizionario3 = {
    1: [0, 1, 2, 3],
    2: [1, 2, 3, 4],
    3: [2, 3, 4, 5]
}
print(dizionario3)

# Non funziona <> LISTE COME CHIAVI NO!
# dizionario4 = {
#     [1,2,3]: "pippo"
# }
# print(dizionario4)

dizionario4 = {
    1: {
        "nome": "Antonio",
        "cognome": "..."
    },
    2: {
        "nome": "Davide",
        "cognome": "..."
    }
}

print(dizionario4)
print(dizionario4[1]['nome'])

diz = {
    (1, 2): "pippo"
}

print(diz)
print(dizionari)
dizionari.update({'ciao': 'asd', 'chiave_completamnete_nuova': 'lol'})
print(dizionari)

dizionari["sole"] = "pippo"
# del dizionari['sole'] # non restituisce il valore
valore = dizionari.pop("sole")  # restitusce il valore della chiave che stiamo rimuovendo
print(valore)

{
    1: []
}

[{1: 1}, {2: 2}]

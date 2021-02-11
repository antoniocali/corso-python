# print("Lezione 4: Funzioni")

def somma(a, b):
    print("Primo Valore: " + str(a))
    print("Secondo Valore: " + str(b))
    print("Somma: " + str(a + b))


# somma(primo_numero, secondo_numero)
#
# primo_valore = input("Dammi un valore")
# secondo_valore = input("Dammi un secondo valore")
# somma(primo_valore, secondo_valore)

# def stampa_nome(nome):
#     print("Ciao " + nome)
#
#
# nome_utente = "Antonio"
# stampa_nome(nome_utente)
# primo_numero = int(input("Dammi un numero"))
# secondo_numero = int(input("Dammi il secondo numero"))
#
#
# def somma2(a, b):
#     return a + b
#
#
# somma_dei_nostri_numeri = somma2(primo_numero, secondo_numero)
# print("La somma e': " + str(somma_dei_nostri_numeri))

# Esercizio 1
# Creare una funzione che si chiama perimetro_triangolo che ha:
#  - 3 parametri che identificano i lati
#  - Restitutisce il perimetro del triangolo
# Una volta creata, chiediamo all'utente di inserire i tre valori dei lati
# E stampiamo a schermo quale e' il perimetro di quel triangolo

def perimetro_triangolo(lato1, lato2, lato3):
    if lato1 > 0 and lato2 > 0 and lato3 > 0:
        return lato1 + lato2 + lato3
    else:
        return -1


lato1 = int(input("Lato 1"))
lato2 = int(input("Lato 2"))
lato3 = int(input("Lato 3"))
"f-string"
stringa = f"lato1 = {lato1}"
perimetro = perimetro_triangolo(lato1, lato2, lato3)
if perimetro > 0:
    print(f"il perimetro del triangolo a lati {lato1}, {lato2}, {lato3}  e' {perimetro}")
else:
    print(f"Il triangolo di lati {lato1}, {lato2}, {lato3} non e' valido")

# Esercizio 2
# Creare una funzione che si chiama area_triangolo che:
# - due paremtri che identificano la base, e l'altezza
# - Restistruisce l'area del triangolo
# Una volta creata la funzione, chiediamo all'utente di inserire i valori dell'altezza e della base
# Stampiamo a schermo quale e' l'area del triangolo

def area_triangolo(base, altezza):
    if base > 0 and altezza > 0:
        return (base * altezza) / 2
    else:
        return -1


base = int(input("base"))
altezza = int(input("altezza"))
print(f"area triangolo di base {base} e altezza {altezza} e' {area_triangolo(base, altezza)}")
# N.B. Per sia Esercizio 1 che Esercizio 2
# Nel corpo della funzione, controllare che tutti i valori che l'utente inserisce sono strettamente positivi
# Se i valori non sono positivi, restiture -1 invece che *il perimetro, o l'area*

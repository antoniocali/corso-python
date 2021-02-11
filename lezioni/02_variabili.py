print("Lezione 02")

# Variabili
nome = "Fulgenzio"
eta = 25
# funzione str -> converte l'oggetto a cui e' applicata in una stringa
print("Mi chiamo " + nome + ", ho " + str(eta) + " anni. Mi chiamo " + nome + " perche' mio nonno si chiamava " + nome + ".")
print("Credo che " + nome + " non sia un gran bel nome.")

# Introduciamo la funzione input
nome_utente = input("Come ti chiami?")
print("Ciao " + nome_utente)

anno_corrente = 2021
anno_utente = int(input("In che anno sei nato? "))
eta_utente = anno_corrente - anno_utente
eta_utente_piu_5 = eta_utente + 5
print("Hai " + str(eta_utente) + " anni. Fra 5 anni avrai " + str(eta_utente_piu_5) + " anni.")

# If-then-else

se (utente regitrato) allora
    mostro_sito
altrimenti
    mostro_presentazione

if utente_registrato:
    carica_carrello
    mostro_sito
else:
    mostro_presentazione
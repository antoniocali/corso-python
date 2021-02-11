# If-then-else

# se (utente regitrato) allora
#     mostro_sito
# altrimenti
#     mostro_presentazione

utente_registrato = True
# if utente_registrato:
#     print('carica_carrello')
#     print('mostro_sito')
# else:
#     print('mostro_presentazione')

print('caricamento sito')
print('caricamento_carrello')
if utente_registrato:
    print('carica_avatar')
print('caricamento_banner_pubblicitario')

# print(1 < 10) # True
# print(1 > 10) # False
# print(5 >= 10) # False
# print(5 >= 5) # True
# print(4 <= 2) # False
# print(4 <= 4) # True
print(3 == 3)

eta_utente = 30
if eta_utente < 18:
    print("Non puoi accedere. Sezione vietata ai minorenni")
else:
    print("Ok. Vai pure Signore")

if True:
    print("Stampero' sempre questa riga.")
else:
    print("Questa linea non sara' mai stampata")

if eta_utente < 18:
    print("Non puoi votare")
else:
    if eta_utente < 25:
        print("Puoi votare alla camera")
    else:
        print("Puoi votare alla camera e al senato")

eta_utente = 13
if eta_utente < 18:
    print("non puoi votare")
elif eta_utente < 25:  # else if
    print("puoi votare solo alla camera")
else:
    print("Puoi votare alla camera e al senato")

if eta_utente >= 0 and eta_utente < 18:
    print("non puoi votare!")
elif eta_utente >= 18 and eta_utente < 25:
    print("puoi votare solo alla camera")
else:
    print("Puoi votare alla camera e al senato")

if eta_utente >= 18 and eta_utente < 25:
    print("puoi votare solo alla camera")
elif eta_utente >= 0 and eta_utente < 18:
    print("Non puoi votare")
else:
    print("Puoi votare alla camera e al senato")

numero_fortunato_utente = 7
if numero_fortunato_utente == 3 or numero_fortunato_utente == 5:
    print("Che tipo cool!")
else:
    print("Non mi parlare!")

# 1. chiedere di inserire un numero all'utente
# 2. Se negativo scrivere a console : negativo
# 3. Se positivo:
#  3.a Se e' 2 o 4 o 6 o 8 o 10: scrivere pari
#  3.b se 1 o 3 o 5 o 7 o 9: scrivere dispari
#  3.c altrimenti scrivere: Non so ancora come fare

# numero_utente = int(input("Dammi un numero"))
# if numero_utente < 0:
#     print("Negativo")
# else:
#     if numero_utente == 2 or numero_utente == 4 or numero_utente == 6 or numero_utente == 8:
#         print("Pari")
#     elif numero_utente == 1 or numero_utente == 3 or numero_utente == 5 or numero_utente == 7 or numero_utente == 9:
#         print("Dispari")
#     else:
#         print("Non sappiamo")

print("opposto a True:" + str(not True))
print("opposto a False:" + str(not False))
if not (numero_fortunato_utente == 5):
    print("Il numer fortunate non e' il 5")
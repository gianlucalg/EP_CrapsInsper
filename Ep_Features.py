import random

#sorteia os numero dos dois dados.
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

soma_dados = dado1 + dado2

dinheiro = 100

aposta = 10

# Função "Twelve", está aposta pode ser feita em qualquer hora do jogo.

def twelve (aposta):

    if soma_dados == 12:
        aposta = aposta*30
    else:
        aposta = 0
    
    return aposta

#print(twelve(aposta))

# Função "Any Craps", está aposta pode ser feita em qualquer hora do jogo.

def any_craps (aposta):

    if soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        aposta = aposta*7
    else:
        aposta = 0
    
    return aposta

#print(any_craps(aposta))

# Função "Field", está aposta pode ser feita em qualquer hora do jogo.

def field (aposta):

    if soma_dados == 5 or soma_dados == 6 or soma_dados == 7 or soma_dados == 8:
        aposta = 0
    elif soma_dados == 3 or soma_dados == 4 or soma_dados == 9 or soma_dados == 10 or soma_dados == 11:
        aposta = aposta + aposta
    elif soma_dados == 2:
        aposta = aposta + aposta*2
    elif soma_dados == 12:
        aposta = aposta + aposta*3

    return aposta

#print(field(aposta))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:20:43 2020

@author: gabrielsalvatorbenatar
"""

import random

# Função "Twelve", está aposta pode ser feita em qualquer hora do jogo.

def twelve (aposta,dinheiro):
    
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma_dados = dado1 + dado2

    if soma_dados == 12:
        aposta = aposta*30
    else:
        aposta = 0
    
    return aposta


# Função "Any Craps", está aposta pode ser feita em qualquer hora do jogo.

def any_craps (aposta,dinheiro):
    
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma_dados = dado1 + dado2
    
    print("A soma dos dados deu {0}".format(soma_dados))

    if soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        dinheiro += aposta*7
        print('Ganhou, a soma deu {0}'.format(soma_dados))
        print("Você tem {0} reais".format(dinheiro))
    else:
        dinheiro-= aposta
        print('Perdeu a soma deu {0}'.format(soma_dados))
        print("Você tem {0} reais".format(dinheiro))
    
    return dinheiro


# Função "Field", está aposta pode ser feita em qualquer hora do jogo.

def field (aposta,dinheiro):
    
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma_dados = dado1 + dado2
    
    print("A soma dos dados deu {0}".format(soma_dados))

    if soma_dados == 5 or soma_dados == 6 or soma_dados == 7 or soma_dados == 8:
        dinheiro -=aposta
        print('Perdeu a soma deu {0}'.format(soma_dados))
        print("Você tem {0} reais".format(dinheiro))
        
    elif soma_dados == 3 or soma_dados == 4 or soma_dados == 9 or soma_dados == 10 or soma_dados == 11:
        dinheiro += aposta
        print('Ganhou, a soma deu {0}'.format(soma_dados))
        print("Você tem {0} reais".format(dinheiro))
        
    elif soma_dados == 2:
        dinheiro += aposta*2
        print('Ganhou, a soma deu {0}'.format(soma_dados))
        print("Você tem {0} reais".format(dinheiro))
        
    elif soma_dados == 12:
        dinheiro += aposta*3
        print('Ganhou, a soma deu {0}'.format(soma_dados))
        print("Você tem {0} reais".format(dinheiro))

    return dinheiro





dinheiro = 100
print("Você tem {0} reais".format(dinheiro))


while dinheiro > 0:
    
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma_dados = dado1 + dado2
    
    opcoes = input("Você quer apostar em field, any_craps ou twelve?")
    
    if opcoes == 'sim' or opcoes == 'Sim':
        qual = input('No que você quer apostar? (f/ac/t) ')
        if qual == 'f':
            aposta = int(input("Quanto você quer apostar?"))
            print(field(aposta,dinheiro))
            opcoes = input("Você quer apostar em field, any_craps ou twelve?")
        
        elif qual == 'ac':
            aposta = int(input("Quanto você quer apostar?"))
            print(any_craps(aposta,dinheiro))
            opcoes = input("Você quer apostar em field, any_craps ou twelve?")
            
        
            
            
            
            
          
            
            
            
            
    print(" ")    
    print("Você está no Come Out")
    aposta = int(input("Quanto você quer apostar?"))
    
    if soma_dados == 7 or soma_dados == 11:
        
        print("A soma dos dados deu {0}".format(soma_dados))
        dinheiro += aposta 
        print("Você tem {0} reais".format(dinheiro))
        
    elif soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        
        print("A soma dos dados deu {0}".format(soma_dados))
        dinheiro -= aposta
        print("Craps")
        print("Você tem {0} reais".format(dinheiro))
        
    else:       
        print("A soma dos dados deu {0}".format(soma_dados))
        print('Você está na fase point')
        point = soma_dados
        print("A soma dos dados precisa dar {0}".format(point))
        soma_dados_point = random.randint(2,12)
        
        while soma_dados_point != point and soma_dados_point!= 7:
            soma_dados_point = random.randint(2,12)
            print("A soma dos dados deu {0}".format(soma_dados_point))
            
        if soma_dados_point == 7:
            print("A soma dos dados deu {0}".format(soma_dados_point))
            dinheiro -= aposta 
            print("Você tem {0} reais".format(dinheiro))
            
        elif soma_dados_point == point:
            print("A soma dos dados deu {0}".format(soma_dados_point))
            dinheiro += aposta 
            print("Você tem {0} reais".format(dinheiro))

print('Acabou! Você faliu! :(' )
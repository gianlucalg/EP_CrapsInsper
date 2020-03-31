#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:20:43 2020

@author: gabrielsalvatorbenatar
"""

import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
soma_dados = dado1 + dado2

dinheiro = 100
print("Você tem {0} reais".format(dinheiro))


while dinheiro > 0:
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
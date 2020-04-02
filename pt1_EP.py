import random

dinheiro = 100
print("Você tem {0} reais".format(dinheiro))


while dinheiro > 0:
     
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma_dados = dado1 + dado2

    if dinheiro > 0:
        opcoes = input("Você quer apostar em field, any_craps ou twelve?")
    
    while opcoes == 'sim' and dinheiro > 0:
        qual = input('No que você quer apostar? (f/ac/t) ')
        if qual == 'f':
            aposta = int(input("Quanto você quer apostar?"))
            

            dado1_f = random.randint(1,6)
            dado2_f = random.randint(1,6)
            soma_dados_f = dado1_f + dado2_f

            if soma_dados_f == 5 or soma_dados_f == 6 or soma_dados_f == 7 or soma_dados_f == 8:
                dinheiro -=aposta
                print('Perdeu, a soma deu {0}'.format(soma_dados_f))
                print("Você tem {0} reais".format(dinheiro))
        
            elif soma_dados_f == 3 or soma_dados_f == 4 or soma_dados_f == 9 or soma_dados_f == 10 or soma_dados_f == 11:
                dinheiro += aposta
                print('Ganhou, a soma deu {0}'.format(soma_dados_f))
                print("Você tem {0} reais".format(dinheiro))
        
            elif soma_dados_f == 2:
                dinheiro += aposta*2
                print('Ganhou, a soma deu {0}'.format(soma_dados_f))
                print("Você tem {0} reais".format(dinheiro))
        
            elif soma_dados_f == 12:
                dinheiro += aposta*3
                print('Ganhou, a soma deu {0}'.format(soma_dados_f))
                print("Você tem {0} reais".format(dinheiro))
            
            if dinheiro > 0:
                opcoes = input("Você quer apostar em field, any_craps ou twelve?")


        
        elif qual == 'ac':
            aposta = int(input("Quanto você quer apostar?"))
            

            dado1_ac = random.randint(1,6)
            dado2_ac = random.randint(1,6)
            soma_dados_ac = dado1_ac + dado2_ac


            if soma_dados_ac == 2 or soma_dados_ac == 3 or soma_dados_ac == 12:
                dinheiro += aposta*7
                print('Ganhou, a soma deu {0}'.format(soma_dados_ac))
                print("Você tem {0} reais".format(dinheiro))
            else:
                dinheiro-= aposta
                print('Perdeu, a soma deu {0}'.format(soma_dados_ac))
                print("Você tem {0} reais".format(dinheiro))

            if dinheiro > 0:
                opcoes = input("Você quer apostar em field, any_craps ou twelve?")



        elif qual == "t":
            aposta = int(input("Quanto você quer apostar?"))


            dado1_t = random.randint(1,6)
            dado2_t = random.randint(1,6)
            soma_dados_t = dado1_t + dado2_t


            if soma_dados_t == 12:
                dinheiro += aposta*30
                print('Ganhou, a soma deu {0}'.format(soma_dados_t))
                print("Você tem {0} reais".format(dinheiro))
            else:
                dinheiro -= aposta
                print('Perdeu, a soma deu {0}'.format(soma_dados_t))
                print("Você tem {0} reais".format(dinheiro))

            if dinheiro > 0:
                opcoes = input("Você quer apostar em field, any_craps ou twelve?")

    if dinheiro <= 0:
        break


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
        print(" ") 
        print('Você está na fase point')
        print(" ") 
        point = soma_dados
        print("A soma dos dados precisa dar {0}".format(point))
        print(" ") 
        soma_dados_point = random.randint(2,12)
        
        while soma_dados_point != point and soma_dados_point!= 7:
            soma_dados_point = random.randint(2,12)
            print("A soma dos dados deu {0}".format(soma_dados_point)) 

        if soma_dados_point == 7:
            print("A soma dos dados deu {0}".format(soma_dados_point))
            dinheiro -= aposta 
            print("Você tem {0} reais".format(dinheiro))
            print(" ") 
            
        elif soma_dados_point == point:
            dinheiro += aposta 
            print("Você tem {0} reais".format(dinheiro))
            print(" ") 

print('Acabou! Você faliu! :(' )
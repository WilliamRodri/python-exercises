import os
import time
import random

def start():
    print("----------------------")
    print("--GERADOR DE SENHAS---")
    print("----------------------")
    a = input("...PRESSIONE ENTER....")
    try:
        if a == "":
            gerador()
        else:
            print("PRECISA DAR UM ENTER")
    except:
        os.system('cls')
        print("erro")

def gerador():
    while True:
        os.system('cls')
        amount = int(input("DE QUANTOS CARACTERES VOCÊ QUER SUA SENHA?: "))
        if amount >= 77:
            print("ERROR, LIMITE MAXIMO TENTE ALGO MENOR QUE 77")
        else:
            lowerCase = 'abcdefghijklmnopqrstuvwxyz'
            uperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            numbers = '0123456789'
            characters = '[]{}()*#;/,-_%'
            junction = lowerCase+uperCase+numbers+characters

            password = "".join(random.sample(junction, amount))

            print(f"Sua senha é {password}")

            time.sleep(1)
            a = input("Deseja gerar outra senha?(s/n)\n: ").lower().strip()[0]

            if a == 's':
                os.system('cls')
                continue
            elif a == 'n':
                os.system('cls')
                break
gerador()
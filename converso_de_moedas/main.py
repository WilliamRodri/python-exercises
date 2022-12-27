import json
import os
import time

with open("file.json", encoding='utf-8') as js:
    data = json.load(js)

    USDBRL = data['USDBRL']
    EURBRL = data['EURBRL']
    BTCBRL = data['BTCBRL']


def start():
    print("----------------------")
    print("REALIZAR SUA CONVERSÃO")
    print("----------------------")
    a = input("...PRESSIONE ENTER....")
    try:
        if a == "":
            print("------------------")
            print("OQUE DESEJA FAZER?")
            res = input(
                "[1]REALIZAR COTAÇÕES\n[2]VER INFORMAÇÕES DE MOEDAS\n[3]SAIR\n: ")
            if res == '1':
                cotacao()
            elif res == '2':
                info()
            elif res == '3':
                os.system('cls')
            else:
                os.system('cls')
                print("PRECISA ESCOLHER UMAS DAS OPÇÕES")
        else:
            print("PRECISA DAR UM ENTER")
    except:
        os.system('cls')
        print("erro")


def info():
    os.system('cls')
    while True:
        print("-----------------------------------")
        print("ESCOLHA UM DAS COTAÇÕES DISPONIVEIS")
        print("[1]USDBRL\n[2]EURBRL\n[3]BTCBRL")
        answer = int(input(": "))

        try:
            if answer == 1:
                print(f"Nome: {USDBRL['name']}\nCotação: {USDBRL['bid']}\nCode: {USDBRL['code']}\nCodeIn: {USDBRL['codein']}")
                time.sleep(1)
                answer_r = input(
                    "DESEJA VER INFORMAÇÕES DE OUTRAS MOEDAS?(s/n)\n: ").lower().strip()[0]
                if answer_r == 's':
                    info()
                elif answer_r == 'n':
                    break
                else:
                    print("DIGITE UMA RESPOSTA CONCRETA!")
            elif answer == 2:
                print(f"Nome: {EURBRL['name']}\nCotação: {EURBRL['bid']}\nCode: {EURBRL['code']}\nCodeIn: {EURBRL['codein']}")
                time.sleep(1)
                answer_r = input(
                    "DESEJA VER INFORMAÇÕES DE OUTRAS MOEDAS?(s/n)\n: ").lower().strip()[0]
                if answer_r == 's':
                    info()
                elif answer_r == 'n':
                    break
                else:
                    print("DIGITE UMA RESPOSTA CONCRETA!")
            elif answer == 3:
                print(f"Nome: {BTCBRL['name']}\nCotação: {BTCBRL['bid']}\nCode: {BTCBRL['code']}\nCodeIn: {BTCBRL['codein']}")
                time.sleep(1)
                answer_r = input(
                    "DESEJA VER INFORMAÇÕES DE OUTRAS MOEDAS?(s/n)\n: ").lower().strip()[0]
                if answer_r == 's':
                    info()
                elif answer_r == 'n':
                    break
                else:
                    print("NÃO ENTENDI")
            else:
                print("DIGITE UMA RESPOSTA CONCRETA!")
        except:
            print("ERROR")


def cotacao():
    while True:
            value_to_be_quoted = float(input("Digite o valor a ser cotado: "))
            ab = int(input("ESCOLHA UMA DAS OPÇÕES ABAIXO\n[1]USDBRL\n[2]EURBRL\n[3]BTCBRL\n[4]OU VER INFORMAÇÕES SOBRE AS MOEDAS\n: "))
            try:
                if ab == 1:
                    r = value_to_be_quoted
                    t = float(USDBRL['bid'])
                    l = r/t
                    print(f"COTAÇÃO ATUAL DO BRL -> USD: {l:.2f}")
                    time.sleep(1)
                    exit = input("DESEJA VER OUTRA COTAÇÃO?(s/n)\n: ").lower().strip()[0]
                    if exit == 's':
                        os.system('cls')
                        continue
                    elif exit == 'n':
                        os.system('cls')
                        break
                elif ab == 2:
                    r = value_to_be_quoted
                    t = float(EURBRL['bid'])
                    l = r/t
                    print(f"COTAÇÃO ATUAL DO BRL -> EUR: {l:.2f}")
                    time.sleep(1)
                    exit = input("DESEJA VER OUTRA COTAÇÃO?(s/n)\n: ").lower().strip()[0]
                    if exit == 's':
                        os.system('cls')
                        continue
                    elif exit == 'n':
                        os.system('cls')
                        break
                elif ab == 3:
                    r = value_to_be_quoted
                    t = float(BTCBRL['bid'])
                    l = r/t
                    print(f"COTAÇÃO ATUAL DO BRL -> BTC: {l:.2f}")
                    exit = input("DESEJA VER OUTRA COTAÇÃO?(s/n)\n: ").lower().strip()[0]
                    if exit == 's':
                        os.system('cls')
                        continue
                    elif exit == 'n':
                        os.system('cls')
                        break
                    elif ab == 4:
                        os.system('cls')
                        start()
                else:
                    os.system('cls')
                    info()
            except Exception as error:
                os.system('cls')
                print("ESCOLHA UMA DAS OPÇÕES", error)
start()
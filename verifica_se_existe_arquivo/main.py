a = input("Nome do Arquivo: ")
if a == 'zen':
    try:
        with open("zen.txt") as file:
            data = file.read()
            print(f"Aqui estar seu texto:\n{data}")
    except Exception as error:
        print(error)
else:
    print("Nao existe um arquivo com esse nome armazenado na minha memoria!")
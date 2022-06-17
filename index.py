import time
import os
import random

armas = {
    "uma Espada": 8,
    "um Arco Longo": 7,
    "uma Katana": 8,
    "uma Adaga": 4,
    "um Arco Curto": 5,
    "um Cajado": 4,
    "uma Lança": 3,
    "uma Faca": 3,
    "uma Maça": 6,
    "um Machado": 9,
    "uma AK47": 8,
} 

curas = {
    "Bandagem": 7,
    "Pomada": 6,
    "Alcool": 3,
    "Kit Médico": 9,
    "Antibióticos": 8,
    "Xarope": 10,
    "Tesoura": 2,
    "Agulha": 4 ,
    "Antiinflamatório": 7,

} 

print("-------------- BEM VINDO(A) --------------")
opcao = input("Para iniciar o jogo, escolha uma opção: \n1- NOVO JOGO\n2- CONTINUAR JOGO SALVO\nSua Resposta --> ")

if opcao == "1":

    sexo = input("Como você deseja ser tratado?\n1- Gerreira\n2- Guerreiro\nSua Resposta --> ")
    if sexo == "1":
        genero = "sua Guerreira"
    else:
        genero = "seu Guerreiro"

    usuario = input(f"\n\nÓtimo! Agora nos diga um nome para {genero} --> " )

    with open(f"{usuario}.text", "w") as arquivo: 
        print("Criado")
        arquivo.write(usuario)
    
    os.system("cls")
 
    print("\n\n\nBOM DIA AVENTUREIRO! Bom... bom... o bom é relativo né...")
    time.sleep(1)
    print("Quando se está em uma Apocalipse é díficil se ter um dia realmente bom....")
    time.sleep(1)
    print("Desde que o vírus se espalhou as pessoas só enlouqueceram e o recurso ficou cada vez mais escasso!")
    time.sleep(1)
    quantitem = 10
    vida = 20
    print("A sua rotina é a mesma a 4 anos... Você acorda e vai coletar recursos, para que sua irmã, Clarisse, não passe fome outra vez...")
    escolha = input("Você acha um item, deseja pega-lo?\n1- SIM\n2- NÃO\nSua Resposta --> ")

    ArmasList = list(armas.keys())
    DanosList = list(armas.values())

    Curas = list(curas.keys())
    QuantCuraList = list(curas.values())

    contador = 0
    ListItensMochila = {"1": 0 }
    ItensMochila = list(ListItensMochila.keys())

    while escolha == "1":
        x = random.randint(0,9)
        ale = random.randint(1,2)

        if ale == 1: 
            itemAtual = ArmasList[x]
            danoAtual = DanosList[x]
            print(f"Você achou {itemAtual}. Com esse item você dará {danoAtual} de Dano!")
            print(f"Você tem {quantitem} de 10 espaços diponíveis em sua mochila!")
            resposta = input("Você deseja colocar esse item na sua mochila?\n1- SIM\n2- NÃO\nSua Resposta --> ")

            if resposta == "1":
                quantitem -=1
                contador = 0
                ItensMochila[contador] = danoAtual
                contador += 1

            os.system("cls")
            print("Você continua andando...")
            escolha = input("Você acha outro item, deseja pega-lo?\n1- SIM\n2- NÃO\nSua Resposta --> ")
        elif ale == 2:
            itemAtual = Curas[x]
            danoAtual = QuantCuraList[x]
            print(f"Você achou {itemAtual}. Com esse item você irá curar {danoAtual} de Vida!")
            print(f"Você tem {vida} de Vida!")
            print(f"Você tem {quantitem} de 10 espaços diponíveis em sua mochila!")
            resposta = input("Você deseja usar esse item e curar?\n1- SIM\n2- NÃO\nSua Resposta --> ")

            if resposta == "1":
                quantitem -=1
                vida += danoAtual
                contador = 0
                ItensMochila[contador] = danoAtual
                contador += 1

            os.system("cls")
            print("Você continua andando...")
            escolha = input("Você acha outro item, deseja pega-lo?\n1- SIM\n2- NÃO\nSua Resposta --> ")

    

        
    
        










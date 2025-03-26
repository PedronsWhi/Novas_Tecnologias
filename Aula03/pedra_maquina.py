import random
elementos = ["Pedra","Papel","Tesoura"]

modo = input("Deseja jogar com a maquina ou outro jogador? (maquina/jogador)")

if modo == "maquina":

    jogador = input("Escolha uma das opções: Pedra, Papel, Tesoura...").strip().capitalize()
    maquina = random.choice(elementos)
    print(f"Você escolheu {jogador} a maquina escolheu {maquina}.")
    if jogador == "Pedra" and maquina == "Tesoura":
        print("Pedra Ganhou")
    elif jogador == "Pedra" and maquina == "Pedra":
        print("Empate")
    elif jogador == "Pedra" and maquina == "Papel":
        print("Papel ganha")

    if jogador == "Tesoura" and maquina == "Pedra":
        print("Pedra Ganhou")
    elif jogador == "Tesoura" and maquina == "Tesoura":
        print("Empate")
    elif jogador == "Tesoura" and maquina == "Papel":
        print("Papel ganha")

    if jogador == "Papel" and maquina == "Tesoura":
        print("Tesoura ganhou")
    elif jogador == "Papel" and maquina == "Pedra":
        print("Papel ganhou")
    elif jogador == "Papel" and maquina == "Papel":
        print("Empate")

if modo == "jogador":
    jogo = input("Qual elemento você deseja jogar? Pedra, Papel, Tesoura")
    jogo2 = input("Selecione outro elemento: Pedra, Papel, Tesoura")

    if jogo == "Pedra" and jogo2 == "Tesoura":
        print("Pedra Ganhou")
    elif jogo == "Pedra" and jogo2 == "Pedra":
        print("Empate")
    elif jogo == "Pedra" and jogo2 == "Papel":
        print("Papel ganha")

    if jogo == "Tesoura" and jogo2 == "Pedra":
        print("Pedra Ganhou")
    elif jogo == "Tesoura" and jogo2 == "Tesoura":
        print("Empate")
    elif jogo == "Tesoura" and jogo2 == "Papel":
        print("Papel ganha")

    if jogo == "Papel" and jogo2 == "Tesoura":
        print("Tesoura ganhou")
    elif jogo == "Papel" and jogo2 == "Pedra":
        print("Papel ganhou")
    elif jogo == "Papel" and jogo2 == "Papel":
        print("Empate")



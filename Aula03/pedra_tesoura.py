maquina = input("Deseja jogar jogo da velha")

if maquina =="sim":
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
else:
    print("Jogo cancelado")


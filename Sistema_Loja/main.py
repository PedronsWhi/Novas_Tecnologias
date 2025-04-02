carrinho = []

def exibir_menu():
    print("Escolha sua opção: ")
    print("1. Frutas")
    print("2. Carnes")
    print("3. Produtos de Limpeza")
    print("4. Ver carrinho")
    print("5. Finalizar compra")

def frutas_estoque():
    Frutas = {
        "1" : {"nome":"Banana" ,"preço": 3.60},
        "2" : {"nome":"Maçã", "preço": 2.50},
        "3" : {"nome": "Pera", "preço": 3.00},
        "4" : {"nome": "Melancia", "preço": 4.00}
    }

    print("FRUTAS")
    for cod, produto in Frutas.items():
         print(f"{cod}. {produto['nome']} - R${produto['preco']:.2f}")
    print("5. Voltar")

    return Frutas


def carnes_estoque():
    Carnes = {
        "1" : {"nome":"Cupim" ,"preço": 22.60},
        "2" : {"nome":"Patinho", "preço": 28.50},
        "3" : {"nome": "Carne de Sol", "preço": 30.00},
        "4" : {"nome": "Picanha", "preço": 40.00}
    }

    print("CARNES")
    for cod, produto in Carnes.items():
         print(f"{cod}. {produto['nome']} - R${produto['preco']:.2f}")
    print("5. Voltar")

    return Carnes


def limpeza_estoque():
    Limpeza = {
        "1" : {"nome":"Venixe" ,"preço": 17.60},
        "2" : {"nome":"Sabão em Pó", "preço": 10.50},
        "3" : {"nome": "Ype", "preço": 12.00},
        "4" : {"nome": "Shampoo", "preço": 16.00}
    }

    print("PRODUTOS DE LIMPEZA")
    for cod, produto in Limpeza.items():
         print(f"{cod}. {produto['nome']} - R${produto['preco']:.2f}")
    print("5. Voltar")

    return Limpeza
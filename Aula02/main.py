# Usando o comando "for"
"""for i in range(10):
   print(i)"""

#Usa-se o "c+=1" para que não vire um looper
"""c = 0
while c < 10:
     print(c)
     c+=1"""

# Usando o termo continue 
"""for i in range(10):
    if i == 5:
        continue
    print(i)"""

#Usando o termo break
"""for i in range(10):
    if i == 5:
        break
    print(i)"""


#arr = [1,2,3,4,5,6,7,8,9,10]
# Esse comando percorre toda a lista e imprime os 3 nomes um de casa vez 
"""arr_names = ["Victor","Zerretos","Fujita"]

for i in arr_names:
    print(i)"""

# Se x e y forem maior que "zero" o comando printa que ambos são positivos
"""x = 10
y = 20

if x > 0 and y > 0:
    print("Amboas x e y são positivos")

if x > 0 or y > 0:
    print("Pelo menos um deles é positivo")

if not x > 0:
    print("x não é maior que 0")"""

# Imprimindo Lista
""""my_list = [1,2,3,4,5,6]"""
"""print(my_list[0:3])
print(my_list[1:4])"""

# Adicionando mais coisas a lista, usa-se o termo "append"
"""my_list.append(6)
print(my_list)"""

# Esse comando adiona um elemento na lista no indice 0 sem remover o elemento que está no indice 0
"""my_list.insert(0,0)
print(my_list)"""

# Esse comando remove um elemento que está na lista 
"""my_list.remove(1)
print(my_list)"""

# Esse comando remove todos os elementos da lista
"""my_list.clear()
print(my_list)"""

# Esse comando reverte a lista 
"""my_list.reverse()
print(my_list)"""

# Ordena os elemento em ordem crescente
"""my_list.sort()
print(my_list)"""

"""my_list.extend([7,8,9])
print(my_list)

print(my_list.count(1))

print(my_list.index[1])"""

# usando Tupla
"""my_tuple = (1,2,3,4,5)
print(my_tuple.index(1))
print(my_tuple.count(1))
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:6])"""

# Usando dicionario 
"""my_dict = {"name": "John", "age": 10, "city": "New York"}
print(my_dict["name"])
print(my_dict.get("age"))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict["age"] = 31
my_dict["country"] = "USA"""

# Usando funções
def my_function(param1, param2):
    return param1 + param2

texto = my_function("Hello ","word!")
print(texto)


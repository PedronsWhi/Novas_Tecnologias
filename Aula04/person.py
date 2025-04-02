class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def pegar_nome(self):
        return self.name
    
    def pegar_idade(self):
        return self.age

    def full_info(self):
        return f"{self.name} tem {self.age} anos de idade"

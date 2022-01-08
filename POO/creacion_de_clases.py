#Creando las clases
class User:
    def __init__(self):
        self.name = 'Michael'
        self.email= 'michael@dojo.com'
        self.account_balance= 0

Guido = User()
Monty = User()

print(Guido.name)
print(Monty.name) #Se imprime el valor de Micheal debido a que eso es lo especificado en la definicion de arriba

Guido.name = 'Guido'
Monty.name = 'Monty'

print(Guido.name)
print(Monty.name) #Se imprime Los nombre debido a que se lo establecio como valor en la linea 14 y 15 

#Dando atributos a la clase 

class User:
    def __init__(self, username, email_adress):
        self.name = username
        self.email= email_adress
        self.account_balance= 0

Guido = User("Guido van Rossum", "guido@python.com")
Monty = User("Monty Python", "monty@python.com")

print(Guido.name)
print(Monty.email)

#Metodos para las clases (deposito)

class User:
    def __init__(self, username, email_adress):
        self.name = username
        self.email= email_adress
        self.account_balance= 0

    def deposito (self, monto):
        self.account_balance += monto

Guido = User("Guido van Rossum", "guido@python.com")
Monty = User("Monty Python", "monty@python.com")

Guido.deposito(10)
Guido.deposito(150)
Monty.deposito(10000)

print(Guido.account_balance)
print(Monty.account_balance)
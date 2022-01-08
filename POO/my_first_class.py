class User:
    def __init__(self, username, email_adress):
        self.name = username
        self.email= email_adress
        self.account_balance= 0 #Creacion de la clase User 

    def deposito (self, monto):
        self.account_balance += monto   #Creacion del metodo para reconocimiento de depositos

    def retiro (self, monto):
        self.account_balance += -monto  #Creacion del metodo para retiros
    
    def transfer (self, other_user, monto):
        self.account_balance+= -monto 
        other_user.account_balance += monto #Creacion del metodo de transferencias bancarias
    
    def display (self):
        print("\n",'*'*50, '\n USER: ', self.name, '\n SALDO:', self.account_balance,'\n','*'*50)
        
    
   
        
#Creacion de las 3 intancias de la clase User 

Kanye = User("Keyne West", "ye@python.com")
Travis = User("Travis Scott", "kactusjack@python.com")
Lebron = User("Lebron James", "kingjames@python.com")

#Haz que el primer usuario haga 3 depósitos y 1 retiro, y luego muestra su saldo
Kanye.deposito(100)
Kanye.deposito(100)
Kanye.deposito(100)

Kanye.retiro(50)

Kanye.display()

#Haz que el segundo usuario haga 2 depósitos y 2 retiros, y luego muestra su saldo

Travis.deposito(50)
Travis.deposito(50)

Travis.retiro(25)
Travis.retiro(25)

Travis.display()

#Haz que el tercer usuario haga 1 depósito y 3 retiros, y luego muestra su saldo

Lebron.deposito(300)

Lebron.retiro(20)
Lebron.retiro(20)
Lebron.retiro(20)

Lebron.display()

#Agrega un método transfer_money; haz que el primer usuario transfiera dinero al tercer usuario y luego imprime los saldos de ambos

Lebron.transfer(Travis,50)

Lebron.display()
Travis.display()


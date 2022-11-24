class Account:
    current_id = 0

    def __init__(self, name, run, mail, password):
        self.id = type(self).current_id
        type(self).current_id += 1
        self.name = name
        self.run = run
        self.mail = mail
        self.password = password
        self.balance = 0

    def deposit(self, ammount):
        if (ammount > 0):
            self.balance += int(ammount)
            return
        print("Debe ser un numero positivo!")

    def withdrawl(self, ammount):
        if (ammount > 0):
            if (ammount <= self.balance):
                self.balance -= int(ammount)
                return
            print("No puede retirar mas de lo que posee!")
        print("Debe ser un numero positivo!")

    def print(self):
        print(f"\nNombre: {self.name}")
        print(f"RUN: {self.run}")
        print(f"Correo: {self.mail}")
        print(f"Balance: {self.balance}")

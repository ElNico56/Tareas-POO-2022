class Account:
    _current_id = 0

    def __init__(self, name, run, mail, password):
        self._id = type(self)._current_id
        type(self)._current_id += 1
        self._name = name
        self._run = run
        self._mail = mail
        self._password = password
        self._balance = 0

    def deposit(self, ammount):
        if ammount > 0:
            self._balance += int(ammount)
            return
        print("Debe ser un numero positivo!")

    def withdraw(self, ammount):
        if ammount > 0:
            if ammount <= self._balance:
                self._balance -= int(ammount)
                return
            print("No puede retirar mas de lo que posee!")
            return
        print("Debe ser un numero positivo!")

    def print(self):
        print(f"\nNombre: {self._name}")
        print(f"RUN: {self._run}")
        print(f"Correo: {self._mail}")
        print(f"Balance: {self._balance}")

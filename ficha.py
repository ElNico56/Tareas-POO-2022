class MedicalRecord:
    def __init__(self, name, bday, weight, height):
        self.name = name
        self.birthday = bday  # YYYY/MM/DD
        self.weight = weight  # in meters
        self.height = height  # in kg
        self.history = ""

    def add_history(self, string):
        self.history += "\n	" + string

    def display(self):
        print("Paciente: " + self.name)
        print("- Fecha nacimiento: " + self.birthday)
        print("- Altura: " + str(self.height))
        print("- Peso: " + str(self.weight))
        print("- Historial medico: " + self.history)


paciente = MedicalRecord("Vincent Vicson", "1995/04/24", 75, 1.75)
paciente.add_history("Sistema inmunatario debil")

paciente.display()
class MedicalRecord:
    def __init__(self, name, bday, weight, height):
        self._name = name
        self._birthday = bday  # YYYY/MM/DD
        self._weight = weight  # in meters
        self._height = height  # in kg
        self._history = ""

    def add_history(self, string):
        self._history += "\n	" + string

    def display(self):
        print("Paciente: " + self._name)
        print("- Fecha nacimiento: " + self._birthday)
        print("- Altura: " + str(self._height))
        print("- Peso: " + str(self._weight))
        print("- Historial medico: " + self._history)


paciente = MedicalRecord("Vincent Vicson", "1995/04/24", 75, 1.75)
paciente.add_history("Sistema inmunatario debil")

paciente.display()

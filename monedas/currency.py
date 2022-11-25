class Country:
    def __init__(self, name, currency, code = None):
        self.name = name
        self.currency = currency
        self.code = code.upper() if code else code

    def set_currency(self, new_currency, new_code):
        self.currency = new_currency
        self.code = new_code.upper() if new_code else new_code

    def print(self):
        print(f"Nombre: {self.name}")
        print(f"Moneda: {self.currency}")
        print(f"Codigo: {self.code}")

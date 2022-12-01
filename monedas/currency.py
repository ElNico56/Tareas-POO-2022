class Country:
    def __init__(self, name, currency, code=None):
        self._name = name
        self._currency = currency
        self._code = code.upper() if code else code

    def set_currency(self, new_currency, new_code):
        self._currency = new_currency
        self._code = new_code.upper() if new_code else new_code

    def print(self):
        print(f"Nombre: {self._name}")
        print(f"Moneda: {self._currency}")
        print(f"Codigo: {self._code}")

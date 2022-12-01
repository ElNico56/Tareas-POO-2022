class Product:
    ## Atributos ##
    _id = 0  # identificador unico
    _name = ""  # nombre
    _stock = 0  # cantidad en stock
    _critical_stock = 0  # cantidad critica
    _price = 0  # precio en pesos
    _retail_price = 0  # precio de venta
    _expiration_date = 0  # fecha de vencimiento
    _supplier = ""  # proveedor
    _notes = ""  # observaciones

    ## Constructor ##
    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self._price = price

    ## Metodos ##
    def update_price(self, price):
        self._price = price

    def add_stock(self, ammount):
        self._stock += ammount

    def set_note(self, note):
        self._note = note


class Supplier:
    ## Atributos ##
    _id = 0  # identificador unico
    _name = ""  # nombre
    _rut = ""  # rol unico trubutario
    _address = ""  # dirección
    _notes = ""  # observaciones

    ## Constructor ##
    def __init__(self, id, name, rut):
        self._id = id
        self._name = name
        self._rut = rut

    ## Metodos ##
    def update_address(self, address):
        self._address = address

    def set_note(self, note):
        self._note = note

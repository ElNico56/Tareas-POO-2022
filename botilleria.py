class Product:
	## Atributos ##
	id = 0 # identificador unico
	name = "" # nombre
	stock = 0 # cantidad en stock
	critical_stock = 0 # cantidad critica
	price = 0 # precio en pesos
	retail_price = 0 # precio de venta
	expiration_date = 0 # fecha de vencimiento
	supplier = "" # proveedor
	notes = "" # observaciones

	## Constructor ##
	def __init__(self, id, name, price):
		self.id = id
		self.name = name
		self.price = price

	## Metodos ##
	def update_price(self, price):
		self.price = price

	def add_stock(self, ammount):
		self.stock += ammount

	def set_note(self, note):
		self.note = note

class Supplier:
	## Atributos ##
	id # identificador unico
	name = "" # nombre
	rut = "" # rol unico trubutario
	address = "" # dirección
	notes = "" # observaciones

	## Constructor ##
	def __init__(self, id, name, rut):
		self.id = id
		self.name = name
		self.rut = rut

	## Metodos ##
	def update_address(self, address):
		self.address = address

	def set_note(self, note):
		self.note = note

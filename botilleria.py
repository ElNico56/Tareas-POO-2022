class Product:
	## Atributos ##
	id = 0 # identificador unico
	name = "" # nombre
	stock = 0 # cantidad en stock
	critical_stock = 0 # cantidad critica
	price = 0 # precio en pesos
	supplier = "" # proveedor
	notes = "" # observaciones miscelaneas

	## Constructor ##
	def __init__(self, id, name, price)
		self.id = id
		self.name = name
		self.price = price

	## Metodos ##
	def set_price(self, price):
		self.price = price

	def add_stock(self, ammount):
		self.stock += ammount

	def f(x):

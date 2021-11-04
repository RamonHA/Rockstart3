from abc import abstractmethod, ABC
from dataclasses import dataclass

@dataclass
class Persona():
	edad: int
	nombre: str
	altura: float
	nacionalidad: str = 'mexicano'

	def __ne__(self):
		pass

esteban = Persona(30, 'esteban', 1.72)
paola = Persona(20, 'paola', 1.62)
paola2 = Persona(20, 'paola', 1.62)
print(esteban)
print(paola)
print(paola2)
print(paola == paola2)


class Electrodomestico(ABC):

	def __init__(self, precio: float, potencia: int, __voltaje):
		self.precio = precio
		self.potencia = potencia
		self.__voltaje = __voltaje

	def prender(self):
		if self.__voltaje > 10:
			print('Se prendio correctamente')
		else:
			print('No tiene suficiente voltaje')
	
	def set_voltaje(self, voltaje):
		self.__voltaje = voltaje

	def get_voltaje(self) -> int:
		return self.__voltaje

	@abstractmethod
	def utilizar_voltaje(self):
		pass


class Pantalla(Electrodomestico):

	def __init__(self, precio, potencia, __voltaje, resolucion):
		Electrodomestico.__init__(self, precio, potencia, __voltaje)
		self.resolucion = resolucion

	def prender(self):
		if self.get_voltaje() < 20:
			print('No existe suficiente voltaje para prender')
		else:
			print('Prendio la pantalla')

	def utilizar_voltaje(self):
		print('Utiliza la mitad voltaje en cada uno de los LEDs')
		print('Utiliza la otra mitad del voltaje para el sonido')
		return super().utilizar_voltaje()

class Estufa_Induccion(Electrodomestico):

	def __init__(self, precio, potencia, __voltaje, magnetismo):
		Electrodomestico.__init__(self, precio, potencia, __voltaje)
		self.magnetismo = magnetismo

	def __str__(self):
		return f"Esta estufa tiene el voltaje de {self.get_voltaje}"

	def __add__(self, otra):
		return f"Esta sumando la estufa {self} + {otra}"
	
	def prender(self):
		if self.get_voltaje() < 120:
			print('No existe voltaje suficiente para calentar')
		else:
			print('Prendio la estufa')

	def utilizar_voltaje(self):
		print('Divide el voltaje entre cada una de las parrillas de la estufa')
		print('Con ese voltaje lo utiliza para calentar el metal conductor del utensilio de cocina')
		return super().utilizar_voltaje()

if __name__ == "__main__":
	print('Metodo principal')

	#Inicializacion de objetos
	tv_samsung = Pantalla(999.99, 3000, 500, 1980)
	estufita = Estufa_Induccion(14.99, 300, 100, 50)
	
	#Obtencion de atributos
	print(tv_samsung.precio)
	print(estufita.precio)

	#Prueba de Encapsulacion
	try:
		print(tv_samsung.__voltaje)
	except Exception as e:
		print('No existe el atributo de ese objeto: ',e)
	
	tv_samsung.set_voltaje(99)
	print(tv_samsung.get_voltaje())

	#Ejecucion de metodos
	tv_samsung.prender()
	estufita.prender()

	#Ejemplo de herencia
	print(f" La television costo ${tv_samsung.precio} \n" +
		f"y tiene resolucion de {tv_samsung.resolucion}")

	#Ejemplo de polimorfismo
	#Overriding o sobreescritura
	tv_samsung.prender()
	estufita.prender()
	#Overloading o sobrecarga
	print('\n')
	print(tv_samsung)
	print(estufita)
	print(estufita + estufita)
	print('\n')

	#Ejemplo abstraccion
	tv_samsung.utilizar_voltaje()
	estufita.utilizar_voltaje()
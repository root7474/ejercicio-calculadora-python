from Modules.Suma import Suma # Importamos a la clase Suma() del módulo Suma.py

# Creamos una clase llamada Multiplicacion() que hereda de la clase Suma()
class Multiplicacion(Suma):
    def __init__(self):
    # Creamos el constructor de la clase que hereda los atributos del constructor de la clase Suma()
        super().__init__()
    
    # Creamos un método get para retornar el valor de __resultado redondeado a 3 decimales
    def getResultado(self):
        return round(self.__resultado)
    
    # Creamos una función multiplicacion() con el parámetro cantidad
    def multiplicacion(self, cantidad):
        self.__resultado = 0 # Igualamos __resultado en 0
        self.__cant = cantidad # Le pasamos el valor de cantidad a __cant
        print() # Hacemos un salto de línea

        # Iteramos con un for() la cantidad de números a multiplicar y calculamos su resultado
        for i in range(self.__cant):
            i += 1 # Incrementamos a la variable i en 1
            self.__numero = self.typeDecimalError(f"Digita el número {i}: ") # __numero será igual al valor que retorne la función typeDecimalError()
            
            if self.__resultado == 0:
                self.__resultado = self.__numero # Si __resultado es igual a 0 le agregamos lo que tenemos en __numero
            else:
                self.__resultado = self.__resultado * self.__numero # Si __resultado ya no es igual a 0, entonces haremos la operación de multiplicación en cada iteración

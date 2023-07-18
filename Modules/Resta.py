from Modules.Suma import Suma # Importamos a la clase Suma() del módulo Suma.py

# Creamos una clase llamada Resta() que hereda de la clase Suma()
class Resta(Suma):
    # Creamos el constructor de la clase que hereda los atributos del constructor de la clase Suma()
    def __init__(self):
        super().__init__()
    
    # Creamos un método get para retornar el valor de __resultado
    def getResultado(self):
        return self.__resultado
    
    # Creamos una función resta() con el parámetro cantidad
    def resta(self, cantidad):
        self.__resultado = 0 # Igualamos __resultado en 0
        self.__cant = cantidad # Le pasamos el valor de cantidad a __cant
        print() # Hacemos un salto de línea

        # Iteramos con un for() la cantidad de números a restar y calculamos su resultado
        for i in range(self.__cant):
            i += 1 # Incrementamos a la variable i en 1
            self.__numero = self.typeDecimalError(f"Digita el número {i}: ") # __numero será igual al valor que retorne la función typeDecimalError()
            
            if self.__resultado == 0:
                self.__resultado = self.__numero # Si __resultado es igual a 0 le agregamos lo que tenemos en __numero
            else:
                self.__resultado = self.__resultado - self.__numero # Si __resultado ya no es igual a 0, entonces haremos la operación de resta en cada iteración

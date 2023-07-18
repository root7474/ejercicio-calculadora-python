from Modules.Suma import Suma # Importamos a la clase Suma() del módulo Suma.py

# Creamos una clase llamada Division() que hereda de la clase Suma()
class Division(Suma):
    # Creamos el constructor de la clase que hereda los atributos del constructor de la clase Suma()
    def __init__(self):
        super().__init__()
    
    # Creamos un método get para retornar el valor de __resultado redondeado a 3 decimales
    def getResultado(self):
        return round(self.__resultado, 3)
    
    # Creamos una función division() con el parámetro cantidad
    def division(self, cantidad):
        self.__resultado = 0 # Igualamos __resultado en 0
        self.__cant = cantidad # Le pasamos el valor de cantidad a __cant
        contador = 0 # Creamos una variable contador
        
        print() # Hacemos un salto de línea

        # Mientras que contador sea menor a __cant, hacemos lo siguiente
        while contador < self.__cant:
            contador += 1 # Incrementamos a nuestro contador en 1
            self.__numero = self.typeDecimalError(f"Digita el número {contador}: ") # __numero será igual al valor que retorne la función typeDecimalError()
            
            try:
                # Hacemos uso de excepciones para evaluar lo que se ha ingresado por consola
                if self.__resultado == 0:
                    self.__resultado = self.__numero # Si __resultado es igual a 0 le agregamos lo que tenemos en __numero
                else:
                    self.__resultado = self.__resultado / self.__numero # Si __resultado ya no es igual a 0, entonces haremos la operación de división en cada iteración
            except ZeroDivisionError:
                print("Error!!!... División por cero") # Si existe una división entre cero se ejecutará este error
                contador = contador - 1 # Le restamos -1 al valor de contador

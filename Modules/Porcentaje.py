from Modules.Suma import Suma # Importamos a la clase Suma() del módulo Suma.py

# Creamos una clase llamada Porcentaje() que hereda de la clase Suma()
class Porcentaje(Suma):
    # Creamos el constructor de la clase que hereda los atributos del constructor de la clase Suma()
    def __init__(self):
        super().__init__()
    
    # Creamos un método get para retornar el valor de __numero
    def getNumero(self):
        return self.__numero
    
    # Creamos un método get para retornar el valor de __resultado
    def getResultado(self):
        return self.__resultado
    
    # Creamos una función porcentaje()
    # Para calcular el porcentaje de un número, hacemos una división entre el mismo número y 100
    def porcentaje(self):
        self.__cant = 100 # A __cant le pasamos un valr de 100
        self.__numero = self.typeDecimalError("Digita un número: ") # __numero será igual al valor que retorne la función typeDecimalError()
        self.__resultado = self.__numero / self.__cant # Hacemos la división entre __numero y __cant y guardamos su resultado dentro de __resultado

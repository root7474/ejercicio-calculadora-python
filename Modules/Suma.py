from Modules.Menu import Menu # Importamos a la clase Menu() del módulo Menu.py

# Creamos una clase llamada Suma() que hereda de la clase Menu()
class Suma(Menu):
    # Creamos el constructor de la clase con los atributos privados __cant, __numero y __resultado
    def __init__(self):
        self.__cant = None # Le pasamos el valor de None a __cant
        self.__numero = None # Le pasamos el valor de None a __numero
        self.__resultado = None # Le pasamos el valor de None a __resultado
    
    # Creamos un método get para retornar el valor de __resultado
    def getResultado(self):
        return self.__resultado
    
    # Creamos una función suma() con el parámetro cantidad
    def suma(self, cantidad):
        self.__resultado = 0
        self.__cant = cantidad # Le pasamos el valor de cantidad a __cant
        print() # Hacemos un salto de línea
        
        # Iteramos con un for() la cantidad de números a sumar y calculamos su resultado
        for i in range(self.__cant):
            i += 1 # Incrementamos a la variable i en 1
            self.__numero = self.typeDecimalError(f"Digita el número {i}: ") # __numero será igual al valor que retorne la función typeDecimalError()
            
            if self.__resultado == 0:
                self.__resultado = self.__numero # Si __resultado es igual a 0 le agregamos lo que tenemos en __numero
            else:
                self.__resultado = self.__resultado + self.__numero # Si __resultado ya no es igual a 0, entonces haremos la operación de suma en cada iteración
    
    # Creamos una función typeDecimalError() para evaluar si se han ingresado caracteres y no valores numéricos
    # A dicha función le pasamos como parámetro una cadena de caracteres (message)
    def typeDecimalError(self, message):
        condicion = False # Creamos una variable condicion que usaremos como condicional para el ciclo while() de esta función
        
        # Mientras que condicion sea igual a False, haremos lo siguiente
        while condicion == False:
            try:
                # Hacemos uso de excepciones para evaluar lo que se ha ingresado por consola
                # A la función input() le pasamos como parámetro lo que halla dentro de message
                userData = eval(input(message)) # Hacemos una conversión numérica de lo que se ingrese por consola
                condicion = True # Si no existe ningún error, condicion será igual a True y se romperá el ciclo
            except (NameError, SyntaxError):
                print("Error!!!... Solo debes ingresar números enteros o decimales") # Este mensaje se ejecutará hasta que se ingrese un valor numérico
        return userData # Retornamos el valor de userData

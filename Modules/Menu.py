# Creamos una clase llamada Menu()
class Menu:
    # Creamos el constructor de la clase con el parámetro nombre con los atributos privados __nombre y __opcion
    def __init__(self):
        self.__nombre = None # Le pasamos el valor de None a __nombre
        self.__opcion = None # Le pasamos el valor de None a __opcion
    
    # Creamos un método set con el parámetro nombre
    def setNombre(self, nombre):
        self.__nombre = nombre # Le pasamos el valor de nombre al atributo __nombre
    
    # Creamos un método get para retornar el valor de __nombre
    def getNombre(self):
        return self.__nombre
    
    # Creamos una función menu() para las opciones
    def menu(self):
        # Importamos las clases de los módulos a usar
        from Modules.Suma import Suma
        from Modules.Resta import Resta
        from Modules.Multiplicacion import Multiplicacion
        from Modules.Division import Division
        from Modules.Porcentaje import Porcentaje
        
        # Hacemos una instancia de dichas clases
        suma = Suma()
        resta = Resta()
        multiplicacion = Multiplicacion()
        division = Division()
        porcentaje = Porcentaje()
        
        # Creamos una variable condicion que usaremos como condicional para el ciclo while() de esta función
        condicion = False

        # Mientras que condicion sea igual a False, haremos lo siguiente
        while condicion == False:
             # __opcion será igual al valor que retorne la función typeIntegerError()
            self.__opcion = self.typeIntegerError(f"\n{self.__nombre} digita una opción:\n"
                                                  "\n1.) Suma."
                                                  "\n2.) Resta."
                                                  "\n3.) Multiplicación."
                                                  "\n4.) División."
                                                  "\n5.) Porcentaje."
                                                  "\n0.) Salir."
                                                  "\n\nOpción: ")
            
            if self.__opcion == 1:
                cantidad = self.typeIntegerError("Digita una cantidad: ") # Pedimos que se ingrese por consola una cantidad y enviamos el valor de esa cantidad a la función typeIntegerError()
                suma.suma(cantidad) # Llamamos a la función suma() de la clase Suma() y le pasamos como parámetro el valor de cantidad
                print(f"\n{self.__nombre} el resultado de la suma es: {suma.getResultado()}") # Imprimimos el resultado de la suma
            elif self.__opcion == 2:
                # Si __opción es igual a 2
                # Hacemos el mismo procedimiento que hicimos con la opción 1
                cantidad = self.typeIntegerError("Digita una cantidad: ") # cantidad será igual al valor que retorne la función typeIntegerError()
                resta.resta(cantidad)
                print(f"\n{self.__nombre} el resultado de la resta es: {resta.getResultado()}") # Imprimimos el resultado de la resta
            elif self.__opcion == 3:
                # Si __opción es igual a 3
                # Hacemos el mismo procedimiento que hicimos con la opción 1
                cantidad = self.typeIntegerError("Digita una cantidad: ")
                multiplicacion.multiplicacion(cantidad)
                print(f"\n{self.__nombre} el resultado de la multiplicación es: {multiplicacion.getResultado()}") # Imprimimos el resultado de la multiplicación
            elif self.__opcion == 4:
                # Si __opción es igual a 4
                # Hacemos el mismo procedimiento que hicimos con la opción 1
                cantidad = self.typeIntegerError("Digita una cantidad: ")
                division.division(cantidad)
                print(f"\n{self.__nombre} el resultado de la división es: {division.getResultado()}") # Imprimimos el resultado de la división
            elif self.__opcion == 5:
                # Si __opción es igual a 5
                porcentaje.porcentaje() # Llamamos a la función porcentaje() de la clase Porcentaje()
                print(f"\n{self.__nombre} el porcentaje de {porcentaje.getNumero()} es: {porcentaje.getResultado()}") # Imprimimos el resultado del porcentaje
            elif self.__opcion == 0:
                print("Hasta pronto...") # Si __opción es igual a 0, imprimimos un mensje de despedida
                condicion = True # condicion será igual a True y se terminará la ejecución del programa
            else:
                print("Error!!!... Opción incorrecta") # Imprimimos un error si se digita una opción incorrecta
    
    # Creamos una función typeIntegerError() para evaluar si se han ingresado caracteres o números decimales
    # A dicha función le pasamos como parámetro una cadena de caracteres (message)
    def typeIntegerError(self, message):
        condicion = False # Creamos una variable condicion que usaremos como condicional para el ciclo while() de esta función
        
        # Mientras que condicion sea igual a False, haremos lo siguiente
        while condicion == False:
            try:
                # Hacemos uso de excepciones para evaluar lo que se ha ingresado por consola
                # A la función input() le pasamos como parámetro lo que halla dentro de message
                userData = int(input(message)) # Hacemos una conversión a enteros de lo que se ingrese por consola
                condicion = True # Si no existe ningún error, condicion será igual a True y se romperá el ciclo
            except ValueError:
                print("Error!!!... Solo debes ingresar números") # Este mensaje se ejecutará hasta que se ingrese un número entero
        return userData # Retornamos el valor de userData

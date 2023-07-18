import sys # importamos al módulo sys
from Modules.Menu import Menu # Importamos a la clase Menu() del módulo Menu.py

class User(Menu):
    def __init__(self):
        super().__init__()
    
    def getNombre(self):
        return self.__nombre
    
    # Creamos una función userData() que se encragará de recibir el nombre del usuario
    def userData(self):
        try:
            # Si no se interrumpe la ejecución del programa
            print("Bienvenido...") # Imprimimos un mensaje de bienvenida
            self.__nombre = self.userDataError("Digita tu nombre: ") # __nombre será igual al valor que retorne la función userDataError()
            
            if self.__nombre.isspace():
                print("Error!!!... Debes digitar tu nombre") # Si el nombre contiene espacios en blanco, lanzaremos un error
            elif len(self.__nombre) <= 2:
                print("El nombre debe contener más de 2 caracteres") # Si el nombre contiene menos de dos caracteres, lanzaremos un error
            else:
                # Si el nombre no contiene espacios en blanco
                self.setNombre(self.__nombre) # Enviamos el valor de self.__nombre a la al método setNombre() de la clase Menu()
                self.menu() # Hacemos una llamada a la función menu() de la clase Menu()
        except  (EOFError, KeyboardInterrupt):
            # Si se interrumpe la ejecución del programa
            print() # Hacemos un salto de línea
            sys.exit() # Llamamos a la función exit() del módulo sys para cerrar la ejcución del programa

    # Creamos una función userDataError() para evaluar si se ha ingresado correctamente el nombre de usuario
    # A dicha función le pasamos como parámetro una cadena de caracteres (message)
    def userDataError(self, message):
        condicion = False # Creamos una variable condicion que usaremos como condicional para el ciclo while() de esta función
        
        # Mientras que condicion sea igual a False, haremos lo siguiente
        while condicion == False:
            userData = input(message) # A la función input() le pasamos el valor del parámetro message
            
            if userData.isspace():
                print("Error!!!... Debes digitar tu nombre") # Si el nombre contiene espacios en blanco, lanzaremos un error
            elif len(userData) <= 2:
                print("El nombre debe contener más de 2 caracteres") # Si el nombre contiene menos de dos caracteres, lanzaremos un error
            else:
                # Si el nombre no contiene espacios en blanco
                condicion = True # Si no existe ningún error, condicion será igual a True y se romperá el ciclo
        return userData # Retornamos el valor de userData

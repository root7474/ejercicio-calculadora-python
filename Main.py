# Programa: Calculadora en consola de Python
# Autor: David Rodríguez

from Modules.User import User # Importamos a la clase User() del módulo User.py

# Creamos una función main() que se encragará de la ejecución del programa
def main():
    user = User()
    user.userData()

if __name__ == "__main__":
    main()

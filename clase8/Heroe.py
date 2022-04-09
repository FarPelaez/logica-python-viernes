# Una clase es un molde
# Declarar una clase (poner sus atributos y métodos)
class Heroe:

    # Constructor de la clase / Es una función especial / Es una función que permite inicializar los atributos
    def __init__(self, name, height):

        # Atributos=Propiedades=Datos ==> Variables del lenguaje que yo elija
        self.nombre = name
        self.poder = None
        self.estatura = height
        self.tipoHeroe = None
        self.cantidadVida = None

    # Métodos=Acciones=¿QuéHaceMiMolde? ==> Funciones del lenguaje que yo elija
    def saludar(self):
        print("Holix")

# Utilizando la clase (crear una instancia=Crear un objeto)
# UN OBJETO SI IMPORTAR EL LENGUAJE ES UNA VARIABLE ESPECIAL


batman = Heroe('Bruce Wayne', 1.90)
joker = Heroe('Unknown', 1.78)

# Con el objeto accedo a un atributo (variable)
print(batman.nombre)
print(joker.poder)

# Con el objeto accedo a un método (función)
batman.saludar()

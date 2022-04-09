class Personaje:
    # Constructor
    def __init__(self):
        # Atributos
        self.__nombre = None
        self.__edad = None

# Un solo guión (_) antes del nombre de la variable = protected
# Dos guiones (__) antes del nombre de la variable = private

    # Método GET (leer/obtener valor de un atributo)
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    # Método SET (escribir/ingresar un valor a un atributo)
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @edad.setter
    def edad(self, edad):
        if (edad < 0):
            print("La edad no puede ser negativa")
        else:
            self.__edad = edad

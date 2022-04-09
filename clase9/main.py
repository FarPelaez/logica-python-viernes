# Importar la clase
from clases.Personaje import Personaje

# Creando objetos
personaje = Personaje("Juan", 800)

# Accediendo a los métodos SET
personaje.nombre = "Katalina"
personaje.edad = -10

# Accediendo a los métodos GET
print(personaje.nombre)
print(personaje.edad)

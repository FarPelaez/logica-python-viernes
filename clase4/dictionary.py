student = {
    'name': 'Camilo',
    'age': 35,
    'isFootballPlayer': 'No'
}

# Imprimir/acceder a todas las llaves/atributos de mi diccionario
print(student)

# Imprimir/acceder a una única llave/atributo de mi diccionario
print(student['name'])
print(student.get('name'))

# Recorrer un diccionario y obtener sus valores
for value in student.values():
    print(value)

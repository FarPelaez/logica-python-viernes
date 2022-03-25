numbers = []
listLenght = 20

for i in range(listLenght):
    number = int(input("Ingrese un número: "))
    numbers.append(number)

searchNumber = int(input("Digite el número que quiere buscar: "))

if (searchNumber in numbers):
    print(f"El número {searchNumber} está en la lista")
else:
    print(f"El número {searchNumber} no está en la lista")

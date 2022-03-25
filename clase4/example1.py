numbers = [1]
listLength = int(input("Ingrese el tamaño de la lista: "))

for i in range(listLength):
    numbers.append((i+1) * 7)

print(numbers)

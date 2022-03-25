cities = []
listLength = 3

for i in range(listLength):
    city = input("Ingrese una ciudad: ")
    cities.append(city)

for y in reversed(cities):
    print(y)

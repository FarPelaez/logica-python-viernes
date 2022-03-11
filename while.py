# Variable Controladora
print("Los quesuditos, palitos de queso")
print("************")
print("0. Digita 0 para salir")
print("1. Digita 1 para calcular el precio de un # de palitos de queso")
print("2. Digita 2 para calcular el precio de un # de empanadas rellenas de queso")
print("3. Digita 3 para ver el precio total de tu pedido")
print("************")

opc = 1
# Declaro el búcle/ciclo/iteración/loop
while(opc != 0):
    opc = int(input("Digita una opción "))
    total = 0

    if (opc == 1):
        num = int(input("¿Cuantos palitos de queso quieres? "))
        item1price = num * 2500
        print(f"Su pedido de {num} palitos cuesta {item1price}")
        total += item1price

    elif (opc == 2):
        num = int(input("¿Cuantas empanadas rellenas de queso quieres? "))
        item2price = num * 4000
        print(
            f"Su pedido de {num} empanadas rellenas de queso cuesta {item2price}")
        total += item2price
    elif (opc == 3):
        print(f"El valor total de su pedido es de {total}")
    elif (opc == 0):
        break
    else:
        print(f"El número ingresado no es válido, por favor intente nuevamente")

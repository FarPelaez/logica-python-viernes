# Ejemplo de estaciones

mes = input("Digite un mes del año").lower()
print(f"El mes digitado fue {mes}")

# Caminos para clasificar el mes
if (mes == "diciembre" or mes == "enero" or mes == "febrero" or mes == "marzo"):
    print(f"Estás en invierno")
elif (mes == "abril" or mes == "mayo"):
    print(f"Estás en primavera")
elif (mes == "junio" or mes == "julio" or mes == "agosto"):
    print(f"Estás en verano")
else:
    print(f"Estás en otoño")

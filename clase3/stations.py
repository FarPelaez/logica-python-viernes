print("Estaciones del año")
print("************")
opc = ()

while(opc != 0):
    mes = input("Digita el mes del año: ")

    if mes.lower() in ('enero', 'febrero', 'marzo'):
        print(f"La estación del año del mes de {mes} es Invierno")
    elif mes.lower() in ('abril', 'mayo', 'junio'):
        print(f"La estacion del año del mes de {mes} es Verano")
    elif mes.lower() in ('julio', 'agosto', 'septiembre'):
        print(f"La estacion del año del mes de {mes} es Otoño")
    elif mes.lower() in ('agosto', 'septiembre', 'octubre'):
        print(f"La estacion del año del mes de {mes} es Primavera")
    else:
        print(f"El dato ingresado no es un mes, por favor intente nuevamente")

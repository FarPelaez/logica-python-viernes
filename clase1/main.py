
nivelAgua = int(input("Digita la cantidad de agua que contiene la represa: "))

if (nivelAgua < 200):
    print("No tengo agua")
elif (nivelAgua >= 200 and nivelAgua < 450):
    print("El nivel del agua está bien")
else:
    print("Se nos vino el embalse D:")

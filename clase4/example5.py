numbersTuple = (50, 45, 20, 30, 40, 87)
numbersList = []

for i in range(len(numbersTuple)):
    if (numbersTuple[i] > 40):
        numbersList.append(numbersTuple[i])

print(numbersList)

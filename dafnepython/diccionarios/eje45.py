palabra = input("Palabra:\n\n")

conteo = {}

for letra in palabra:
    if letra in conteo:
        conteo[letra] += 1
    else:
        conteo[letra] = 1

for letra, cantidad in conteo.items():
    print(f"{letra} : {cantidad}")
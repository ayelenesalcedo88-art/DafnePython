segundos = int(input("Ingrese la cantidad de segundos: "))
minutos = segundos // 60
horas = minutos // 60
print(f"{segundos} segundos son {horas} horas, {minutos % 60} minutos y {segundos % 60} segundos.")
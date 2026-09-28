nombres = []
tiempos =[]
while True:
    print("========MENU=======")
    print("1. registrar deportista")
    print("2. mostrar deportistas")
    print("3. buscar deportista")
    print("4. mostrar tiempo ")
    print("5. mostrar tiempo promedio")
    print("6. salir")
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        nombre = input("Ingrese el nombre del deportista: ")
        tiempo = float(input("Ingrese el tiempo del deportista: "))
        nombres.append(nombre)
        tiempos.append(tiempo)
    if opcion == 2:
        print("Lista de deportistas: ")
        for i in range(len(nombres)):
            print(f"{nombres[i]} - {tiempos[i]} segundos")
        if nombres == []:
            print("No hay deportistas registrados")
    if opcion == 3:
        nombre_buscar = input("Ingrese el nombre del deportista a buscar: ")
        for i in range(len(nombres)):
            if nombres[i] == nombre_buscar:
                print(f"{nombres[i]} - {tiempos[i]} segundos")
                break
        else:
            print("Deportista no encontrado")

    if opcion == 4:
        if tiempos:
            menor = tiempos[0]
            posicion = 0
            for i in range(len(tiempos)):
                if tiempos[i] < menor:
                    menor = tiempos[i]
                    posicion = i
            print(f"El mejor tiempo es: {menor} segundos, obtenido por {nombres[posicion]}")
        else:
            print("No hay tiempos registrados")
    if opcion == 5:
        if tiempos:
            promedio = sum(tiempos) / len(tiempos)
            print(f"El tiempo promedio es: {promedio} segundos")
        else:
            print("No hay tiempos registrados")
    if opcion == 6:
        print("has salido del programa")
        break
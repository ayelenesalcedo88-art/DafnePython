cantidad = int(input("Ingrese la cantidad de estudiantes: "))
estudiantes = {}

for i in range(cantidad):
    codigo = input(f"Código del estudiante {i+1}> ")
    nombre = input(f"Nombre del estudiante {i+1}> ")
    edad = int(input(f"Edad del estudiante {i+1}> "))
    carrera = input(f"Carrera del estudiante {i+1}> ")
    promedio = float(input(f"Promedio del estudiante {i+1}> "))
    
    estudiantes[codigo] = {
        "Nombre": nombre,
        "Edad": edad,
        "Carrera": carrera,
        "Promedio": promedio
    }
    print()

mejorCodigo = ""
mayorPromedio = -1.0

for codigo, datos in estudiantes.items():
    if datos["Promedio"] > mayorPromedio:
        mayorPromedio = datos["Promedio"]
        mejorCodigo = codigo

print("Mejor estudiante\n")
if mejorCodigo:
    datosMejor = estudiantes[mejorCodigo]
    print(f"Código: {mejorCodigo}")
    print(f"Nombre: {datosMejor['Nombre']}")
    print(f"Edad: {datosMejor['Edad']}")
    print(f"Carrera: {datosMejor['Carrera']}")
    print(f"Promedio: {datosMejor['Promedio']}")
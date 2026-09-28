edad = int (input("Ingrese su edad: \n"))
if edad < 12:
    print(f"edad: {edad}")
    print("clafificacion : niño")
elif edad >= 12 and edad < 18:
    print(f"edad: {edad}")
    print("clasificacion : adolescente")
else: 
    print(f"edad: {edad}")
    print("clasificacion : adulto")
    if edad >= 60:
        print(f"edad: {edad}")
        print(f"clasificacion : adulto mayor")
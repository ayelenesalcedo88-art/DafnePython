cantidad = int(input("Ingrese la cantidad de libros: "))
biblioteca = {}

for i in range(cantidad):
    codigo = input(f"Código del libro {i+1}> ")
    titulo = input(f"Título del libro {i+1}> ")
    biblioteca[codigo] = titulo

print()
consultar = input("Ingrese el código a consultar> ")

print("\nLibro encontrado:\n")
if consultar in biblioteca:
    print(f"{consultar} -> {biblioteca[consultar]}")
else:
    print(f"El código {consultar} no existe en la biblioteca.")
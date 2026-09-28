agenda = {}

cantidad = int(input("Cantidad de contactos: "))
print()

for _ in range(cantidad):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono
    print()

buscar = input("Buscar contacto: ")

if buscar in agenda:
    print(f"Teléfono de {buscar}: {agenda[buscar]}")
else:
    print(f"El contacto {buscar} no se encuentra en la agenda.")
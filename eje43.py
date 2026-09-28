inventario = {}

cantidad = int(input("Cantidad de productos: "))
print()

for _ in range(cantidad):
    producto = input("Producto: ")
    unidades = int(input("Cantidad: "))
    inventario[producto] = unidades
    print()

consultar = input("Consultar producto: ")

if consultar in inventario:
    print(f"Cantidad disponible de {consultar}: {inventario[consultar]}")
else:
    print(f"El producto {consultar} no se encuentra en el inventario.")
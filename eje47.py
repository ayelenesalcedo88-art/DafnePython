cantidad = int(input("Ingrese la cantidad de vendedores: "))
ventas = {}

for i in range(cantidad):
    vendedor = input(f"Nombre del vendedor {i+1}> ")
    total = int(input(f"Total vendido por el vendedor {i+1}> "))
    ventas[vendedor] = total

mejorVendedor = ""
mayorVenta = -1

for vendedor, total in ventas.items():
    if total > mayorVenta:
        mayorVenta = total
        mejorVendedor = vendedor

print("\nMayor vendedor:\n")
print(f"{mejorVendedor} -> ${mayorVenta}")
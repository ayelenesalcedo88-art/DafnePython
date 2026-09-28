cantidad = int(input("Ingrese la cantidad de empleados: "))
empleados = {}

for i in range(cantidad):
    identificacion = input(f"Identificación del empleado {i+1}> ")
    salario = float(input(f"Salario del empleado {i+1}> "))
    empleados[identificacion] = salario

suma_salarios = 0
for salario in empleados.values():
    suma_salarios += salario

promedio = suma_salarios / cantidad if cantidad > 0 else 0

print(f"\nSalario promedio: ${promedio:.2f}")
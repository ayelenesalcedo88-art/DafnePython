comensales = int(input(" ¿para cuantas personas es la tortilla? "))
patatas_gramos=200 * comensales
huevos = ( patatas_gramos * 5) // 1000
cebolla_gramos = (patatas_gramos * 300) // 1000
print(" -------- INGREDIENTES NECESARIOS ---- ")
print(f"Patatas: {patatas_gramos} gramos")
print(f"Huevos: {huevos}")
print(f"Cebolla: {cebolla_gramos} gramos")
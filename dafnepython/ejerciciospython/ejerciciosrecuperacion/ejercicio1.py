precio_base = float(input("Ingrese el precio base del producto: "))
porcentaje_iva = float(input("Ingrese el porcentaje del iva :"))
monto_iva = precio_base * (porcentaje_iva / 100)
precio_final = precio_base + monto_iva
print("el precio final del producto es : ", precio_final)





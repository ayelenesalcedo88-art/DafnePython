valor_compra = int(input("Ingrese el valor de la compra: \n"))
if valor_compra > 500000:
    if not valor_compra < 500000:
        print(" su total a pagar es: ", valor_compra)
    print("el valor de la ocmpra es mayor a 500000, por lo tanto se le aplicará un descuento del 10%")
    valor_descuento = valor_compra * 0.10
    valor_final = valor_compra - valor_descuento
    print(f"el total a pagar es: {valor_compra}")
    print(f"valor del descuento: {valor_descuento}")
    print(f"valor final: {valor_final}")
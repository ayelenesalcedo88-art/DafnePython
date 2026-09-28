lado1= int(input("Ingrese el primer lado del triangulo: \n"))
lado2= int(input("Ingrese el segundo lado del triangulo: \n"))
lado3= int(input("Ingrese el tercer lado del triangulo: \n"))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Los lados ingresados pueden formar un triangulo")
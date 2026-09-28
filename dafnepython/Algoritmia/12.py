numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número: "))
numero3=int(input("Ingrese el tercer número: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"El número mayor es: {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El número mayor es: {numero2}")
else:
    print(f"El número mayor es: {numero3}")
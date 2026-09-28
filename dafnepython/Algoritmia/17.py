print(" que operacion desea hacer: \n 1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. Division")
operacion=int(input("Ingrese el número de la operación que desea realizar: "))
numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número: "))

if operacion == 1:
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == 2:
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {resultado}")  
if operacion == 3:
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicacion es: {resultado}")
elif operacion == 4:
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de la division es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
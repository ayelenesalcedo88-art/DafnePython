palabra = input("escriba una palabra:")
vocales = "aeiouAEIOU"
contador = 0
for letra in palabra:
    if letra in vocales:
        contador += 1
        print(f"La letra '{letra}' es una vocal.")
print(f"El número total de vocales en la palabra '{palabra}' es: {contador}")
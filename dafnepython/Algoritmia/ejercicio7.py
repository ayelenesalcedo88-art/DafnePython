edad = int(input("Ingrese su edad: \n"))
if edad < 18:
    print("no puedes entrar a la discoteca")    
else:
    tiene_dinero = bool(int(input("¿Tiene dinero? (1 para sí, 0 para no): \n")))
    if tiene_dinero:
        print("puedes entrar a la discoteca")
    else:
        print("no puedes entrar a la discoteca")

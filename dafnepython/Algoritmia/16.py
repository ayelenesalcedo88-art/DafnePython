año = int(input("Ingrese el año: \n"))
if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")
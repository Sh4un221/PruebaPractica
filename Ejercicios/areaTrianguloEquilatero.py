#base*altura/2
base=float(input("Ingrese la base: "))
altura=float(input("Ingrese la altura: "))
area=(base*altura)/2
if(area>1000):
    print("<DATOS NO VALIDOS=")
else:
    print("El area del triangulo equilatero con la medida de la altura ",altura," y la medida de la base ",base," es de ",(altura*base)/2)

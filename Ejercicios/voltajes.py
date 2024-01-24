voltajes=[]
prom=0
sumV=0
for i in range(0,5,1):
    vol=float(input("Ingrese el valor del voltaje: "))
    voltajes.append(vol)
    sumV+=vol
prom=sumV/len(voltajes)
if(prom>220):
    print("<ALTO VOLTAJE=")
else:
    print("<VOLTAJE CORRECTO=")


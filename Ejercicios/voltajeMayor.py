voltajes=[]
prom=0
sumV=0
for i in range(0,3,1):
    vol=float(input("Ingrese el valor del voltaje: "))
    voltajes.append(vol)
    sumV+=vol
prom=sumV/len(voltajes)
if(prom<115):
    print("<VOLTAJE CORRECTO=")
elif((prom>115)and(prom<220)):
    print("<ALTO VOLTAJE=")
elif(prom>220):
    print("<PELIGRO=")



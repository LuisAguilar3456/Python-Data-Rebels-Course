import numpy as np
print("Actividad basica:")
val=1
suma=0
while val!=0:
    val=int(input("Ingresa el monto de compra:"))
    if val>=0:
        suma=suma+val
    else:
        print("No se pueden ingresar numeros negativos")
        val=int(input("Ingrese otra cantidad:"))
        suma=suma+val
print("")
print("El total de la compra fue:",suma)
if suma>1000:
    suma=suma*(1-0.1)
    print("Se le aplico un descuento del 10%")
    print("Resultando un total de:",suma)
print("")
################################################################################################################
def Estacionamiento(val,suma):
    while val!=0:
        val=int(input("Ingresa el tiempo en el estacionamiento:"))
        if val>=0:
            suma=suma+val
        else:
            print("No se pueden ingresar numero negativos")
            continue
    return(suma)
print("Actividad Avanzada")
val=1
suma=0
Tiempo=Estacionamiento(val,suma)
print("")
Tiempo/=60
print("Usted estuvo",Tiempo,"horas en el estacionamiento")
if Tiempo<=1:
    Tarifa=25
elif Tiempo<=8:
    Tarifa=25+(np.ceil(Tiempo)-1)*15
else:
    Tarifa=225+(np.ceil(Tiempo)-1)*15
print("Usted debe de pagar: $",Tarifa)

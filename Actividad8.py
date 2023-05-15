import numpy as np
import random 
print("Actividad basica:")
Diccionario={"Luis":1,"Venus":2,"Cristina":3,"Larissa":4,"Mariana":5}
print("El diccionario original es:",Diccionario)
Valores=list()
for nombre,numero in Diccionario.items(): #Un for con dos variables utilizando .items
    print(nombre,numero)
    Valores.append(numero)
minimo=np.min(Valores) #Calcula el minimo de la lista Valores
maximo=np.max(Valores) #Calcula el maximo
print("El valor minimo es:",minimo) 
print("El valor maximo es:",maximo)
print("")
################################################################################################
print("Actividad Avanzada con Random")
Nombres=["Luis","Venus","Cristina","Larissa","Mariana"]
Diccionario=dict()
Valores=list()
Diccionario={nombre:random.randint(1,10) for nombre in Nombres}
print(Diccionario)
for x in Diccionario: #Ciclo for de una variable normal 
    print(x,Diccionario[x]) #x representa la clave en el ciclo y Diccionario[x] represnata el valor de la clave 
    Valores.append(Diccionario[x])
minimo=np.min(Valores)
maximo=np.max(Valores)
print("El valor minimo es:",minimo)
print("El valor maximo es:",maximo)
print("")

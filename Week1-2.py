print("Listas:")
lista1=["Zanahoria","aguacate","Pizza","Hamburguesa"]
print("Lista original",lista1)
lista1.append("Alitas")
print("Lista modificada:",lista1)
print("Primer elemento de la lista:",lista1[0]) #Imprime el primer valor de la lista 
print("Ultimo elemento de la lista:",lista1[len(lista1)-1]) #Imprime el ultimo valor de la lista
print("")
#######################################################################################################
print("Diccionarios:")
dicc={"Luis":7224929293,"Cristina":7225226651,"Venus":7223054524}
print(dicc.get("Luis"))
print(dicc["Venus"])
IT=dicc.items()
print("Tuplas del diccionario:",IT) #Se dan los pares de llaves y valores
Key=dicc.keys()
print("Las llaves son:",Key) #Se imprimen la llaves  
Vals=dicc.values()
print("Los valores son:",Vals) #Se imprimen los valores de las llaves
dicc.update({"Mariana":7226065502}) #Se agregan valores al diccionario
print("El diccionario actualizado:",dicc)
print("")
#########################################################################################################
print("Tuplas:")
Tupla1=(1,2,[3,4,5],2,2,2,"Hello")
print("La tupla inicial:",Tupla1)
print(Tupla1.count(2)) #Busca cuantas veces hay #2 en la tupla 
print(Tupla1.count("Hello")) #Busca cuantas veces hay "Hello" en tupla
print(Tupla1.index("Hello")) #Busca la posición de "Hello" en la tupla 
print("")
#########################################################################################################
print("Sets:")
MySet={1,2,3,4,5,6,7,8,9}
print("Set original:",MySet)
MySet.add(1540)
print("Set modificado:",MySet)
MySet.discard(5)
print("Set con elemento borrado:",MySet)
MySet2={10,11,12,13,14,15}
print("Set #2:",MySet2)
MySet=MySet.union(MySet2)
print("Union de MySet y MySet2:",MySet)

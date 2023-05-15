def sumNumeros(Numero1,Numero2):
    suma=Numero1+Numero2
    return suma
print("Funciones:")
sumas=sumNumeros(3,2)
print("Utiliza la función sumNUmeros:",sumas)
print("")
################################################################################################
a="luis"
print(a)
print("Utiliza la función .upper:",a.upper())
print("")
################################################################################################
print("")
print("Clases")
class Perro:
    raza="No definido"
    color="No definido"
Perrito=Perro()
print("Antes de modificar valores")
print("Raza:",Perrito.raza,"Color:",Perrito.color)
Perrito.raza="Pug"
Perrito.color="Cafe"
print("Despues de modificar valores")
print("Raza:",Perrito.raza,"Color:",Perrito.color)

edad=float(input("Ingresa tu edad: "))

if edad>=18:
    print("Felicidades eres mayor de edad")
else:
    print("Lo lamento eres menor de edad")
    
nombre1=input("Ingresa el nombre de la primer persona: ")
edad1=float(input("Ingresa la edad de la primer persona: "))
nombre2=input("Ingresa el nombrede la segunda persona: ")
edad2=float(input("Ingresa la edad de la sgunda persona: "))

if edad1>edad2:
    print(nombre1,"es mayor que",nombre2,"con",edad1,"años de edad")
elif edad2>edad1:
    print(nombre2,"es mayor que",nombre1,"con",edad2,"años de edad")
else:
    print(nombre1,"y",nombre2,"tienen la misma edad con",edad1,"años")
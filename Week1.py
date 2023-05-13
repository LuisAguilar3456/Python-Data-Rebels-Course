txt="luis AGUILAR MORENO" #Texto original
print("Original: "+txt)
Cap=txt.capitalize() #Primera letra mayuscula
print("Capitalize: "+Cap)
low=txt.lower() #Todo minusculas 
print("Minusculas: "+low)
may=txt.upper() #Todo mayusculas
print("Mayusculas: "+may)
rep=txt.replace("is","isa") #Remplazar una parte de texto por otro 
print("Replace: "+rep)
nombre="luis"
paterno="aguilar"
materno="moreno"
FullName=nombre.capitalize()+" "+paterno.upper()+" "+materno.upper() #Concatenar textos 
print("Nombre Completo: "+FullName)
print("La longitud de FullName:",len(FullName)) #Medir logitud de la variable 
print(type(FullName)) #Checar tipo de variable 
Romper=FullName.split(" ") #Dividir variable en elementos de una lista
print("Se crea una lista con FullName")
print(Romper)
print(type(Romper))
print(len(Romper)) #Medir longitud de lista 
print("")
#######################################################################################################
Num=[1,2,3,4,5]
print("For in",Num) #Ciclo For para una lista
for i in Num:
    print(i)
print("For in range",len(Num)) #Ciclo For con n contados
for x in range(len(Num)):
    print(x)
print("")
print("Aumento cada 2, de 0-10")
for y in range(0,10,2): #Ciclo For de 0 a 10 con avance cada 2
    print(y)
x=1
print("")
print("Ciclo While con tope hasta 10")
while x<=10: #Ciclo While con tope hasta 10
    print(x)
    x=x+1
print("")
###########################################################################################################
a=3
b=3
print("Uso de if, elif y else en un condicional")
print("a:",a,"b:",b)
if a>b: #Condicionales IF
    print("a es mayor que b")
elif b>a:
    print("b es mayor que a")
else:
    print("a es igual que b")
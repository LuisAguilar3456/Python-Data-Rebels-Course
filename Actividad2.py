x=int(1)
y=float(2.0)
z=True
w="Luis"
v=2+5j
MiTupla=(v,w,x,y,z)
print("La Tupla inicial es:",MiTupla,type(MiTupla))
MiLista=list(MiTupla)
print("Tupla transformada a lista:",MiLista,type(MiLista))
Diccionario=dict()
for i in range(1,6):
    Diccionario[i]=MiLista[i-1]
print("El diccionario creado fue:",Diccionario)
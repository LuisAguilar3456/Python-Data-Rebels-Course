import numpy as np
def Cuadratica(a,b,c):
    if (b**2)>=(4*a*c):
        x1=(-b+np.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-np.sqrt(b**2-4*a*c))/(2*a)
    else:
        i=np.sqrt(-(b**2-4*a*c))/(2*a)
        j=-b/(2*a)
        x1=str(j)+"+"+str(i)+"j"
        x2=str(j)+"-"+str(i)+"j"
        print("Las raices son imaginarias")
    return(x1,x2)
print("")
a=int(input("Ingresa el valor de a: "))
b=int(input("Ingresa el valor de b: "))
c=int(input("Ingresa el valor de c: "))
[x1,x2]=Cuadratica(a,b,c)
print("x1:",x1,"x2:",x2)
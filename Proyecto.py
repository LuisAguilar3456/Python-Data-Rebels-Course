from datetime import datetime 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#########################FUNCIÓN PARA INGRESAR CLIENTES A LA BASE DE DATOS#############################
def ingresar(df):
    print("Se procedera a hacer el registro del cliente")
    print("Por favor introduzca los siguientes datos")
    print("")
    Nombre=input("Ingrese su nombre completo: ")
    Edad=float(input("Ingrese su edad: "))
    Genero=input("Ingrese su genero ('M' ó 'F'): ")
    Pago=input("Ingrese cual sera su metodo de pago ('Efectivo' ó 'Tarjeta'): ")
    Nacionalidad=input("Ingrese su país de origen: ")
    Ciudad=input("Ingrese la ciudad en la que actualmente vive: ")
    Fecha_Registro=datetime.today().date()
    Nuevo_Cliente=[Nombre,Edad,Genero,Pago,Nacionalidad,Ciudad,Fecha_Registro]
    Nuevo_Cliente=pd.DataFrame({'Nombre':[Nuevo_Cliente[0]],'Edad':[Nuevo_Cliente[1]],'Genero':[Nuevo_Cliente[2]],
                                    'Metodo de Pago Preferido':[Nuevo_Cliente[3]],'Nacionalidad':[Nuevo_Cliente[4]],
                                    'Ciudad':[Nuevo_Cliente[5]],'Fecha de Registro':[Nuevo_Cliente[6]]})
    df=pd.concat([df,Nuevo_Cliente],ignore_index=True)
    return (df)
#####################FUNCIÓN PARA ENCONTRAR PRODUCTO#####################
def indice(lista,producto):
    try:
        ind=lista.index(producto)
        return ind
    except ValueError:
        ind=-1
        return ind
#####################FUNCIÓN PARA REGISTAR COMPRA#######################
def Historial(df,Cliente,producto,cantidad,total,metodo):
    Fecha=datetime.today().date()
    Hora=datetime.now().strftime("%H:%M:%S")
    Nuevo_Registro=pd.DataFrame({"Fecha":[Fecha],"Hora":[Hora],"Cliente":[Cliente],
                                 "Producto":[producto],"Cantidad":cantidad,"Costo total":total,"Metodo de Pago":[metodo]})
    df=pd.concat([df,Nuevo_Registro],ignore_index=True)
    return (df)

##################################CODIGO FUENTES################################
Excel_Productos=pd.read_excel('Productos.xlsx')
Clientes=pd.read_excel('ClientesProyecto.xlsx')
Historial_Clientes=pd.read_excel('HistorialCompras.xlsx')
Productos=Excel_Productos["PRODUCTO"].to_list()
Precio_Productos=Excel_Productos["PRECIO"].to_list()
Cantidad_Productos=Excel_Productos["CANTIDAD"].to_list()
print("Presione 'Y' en caso de que su respuesta sea afirmativa y 'N' en caso de ser negativa")
TieneCuenta=input("¿Usted tiene cuenta con esta empresa: ")
print("")
while TieneCuenta!="Y":
    if TieneCuenta=="N":
        Clientes=ingresar(Clientes)
        Clientes.to_excel(r'\Users\dell\Documents\Python Data Rebels\Python-Data-Rebels-Course\ClientesProyecto.xlsx', index=False)
        TieneCuenta="Y"
    else:
        print("Su respuesta es invalida")
        print("")
        TieneCuenta=input("¿Usted tiene cuenta con esta empresa: ")
        continue

print("Bienvenido a la tienda")
Nombre=input("Me puede proporcionar su nombre de registro: ")
Cliente_Actual=Clientes[Clientes["Nombre"]==Nombre]
Num_Clientes=len(Cliente_Actual)
i=1
while Num_Clientes<1:
    print("Lo lamento, no lo pudimos encontrar")
    Nombre=input("Me puede repetir su nombre de registro: ")
    Cliente_Actual=Clientes[Clientes["Nombre"]==Nombre]
    Num_Clientes=len(Cliente_Actual)
    i=i+1
    if i==5:
        print("Lo lamento mucho, procederemos a registrarlo")
        Clientes=ingresar(Clientes)
        Clientes.to_excel(r'\Users\dell\Documents\Python Data Rebels\Python-Data-Rebels-Course\ClientesProyecto.xlsx', index=False)
        Cliente_Actual=Clientes.tail(1)
        Num_Clientes=1
print("")
print("")
print("El cliente actual es:")
print(Cliente_Actual)
print("")
print("")
print("Presione 'Y' en caso de que su respuesta sea afirmativa y 'N' en caso de ser negativa")
Deseo_Compra=input("¿Desea comprar alguno de nuestros productos? ")
print("")
print("")
Compra_Total=0
Cantidad_Toltal=0
while Deseo_Compra!="N":
    print("Nuestro productos son:")
    print(Productos)
    print("")
    Interes=input("Ingrese el nombre del producto que desea comprar: ")
    Index_Interes=indice(Productos,Interes)
    if Index_Interes>-1:
        print("El precio de",Interes,"es: $",Precio_Productos[Index_Interes])
        Cantidad_Compra=int(input("¿Cuantas piezas deseas comprar? "))
        while Cantidad_Compra<1:
            print("No se puede ingresar esa cantidad, por favor ingrese una cantidad mayor que 1")
            Cantidad_Compra=int(input("¿Cuantas piezas deseas comprar? "))
            print("")
        Cantidad_ActualInteres=Cantidad_Productos[Index_Interes]
        while Cantidad_Compra>Cantidad_ActualInteres:
            print("")
            print("Lo lamento, solo contamos con",Cantidad_ActualInteres,"de",Interes)
            Cantidad_Compra=int(input("¿Cuantas piezas deseas comprar? "))
        Cantidad_Productos[Index_Interes]=Cantidad_Productos[Index_Interes]-Cantidad_Compra
        Cantidad_Toltal=Cantidad_Toltal+Cantidad_Compra
        Compra_Total=Compra_Total+Cantidad_Compra*Precio_Productos[Index_Interes]
        Historial_Clientes=Historial(Historial_Clientes,Cliente_Actual["Nombre"].to_list()[0],
                                     Interes,Cantidad_Compra,Cantidad_Compra*Precio_Productos[Index_Interes],
                                     Cliente_Actual["Metodo de Pago Preferido"].to_list()[0])
        print("")
        print("La cantidad de su compra es:",Compra_Total)
        print("")
        print("")
        print("Presione 'Y' en caso de que su respuesta sea afirmativa y 'N' en caso de ser negativa")
        Deseo_Compra=input("¿Desea comprar otro articulo? ")
        print("")
        print("")
    else:
        print("No se pudo encontrar ese articulo")
        print("")
        print("Presione 'Y' en caso de que su respuesta sea afirmativa y 'N' en caso de ser negativa")
        Deseo_Compra=input("¿Desea comprar algún articulo? ")
        print("")

print("Muchas gracias por su visita")
print("Usted gasto $",Compra_Total,"en",Cantidad_Toltal,"articulos")
Productos=pd.DataFrame({"PRODUCTO":Productos,"PRECIO":Precio_Productos,"CANTIDAD":Cantidad_Productos})
Productos.to_excel(r'\Users\dell\Documents\Python Data Rebels\Python-Data-Rebels-Course\Productos.xlsx', index=False)
Historial_Clientes.to_excel(r'\Users\dell\Documents\Python Data Rebels\Python-Data-Rebels-Course\HistorialCompras.xlsx', index=False)








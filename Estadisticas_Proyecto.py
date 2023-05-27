import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Excel=pd.read_excel('HistorialCompras.xlsx')
Excel_Clientes=pd.read_excel('ClientesProyecto.xlsx')
print(Excel.info())
##################ANALISIS METODO DE PAGO########################
print("")
print("")
print("ANALISIS METODOS DE PAGO")
Pago=Excel.copy()
Pago=Pago["Metodo de Pago"].value_counts().to_frame().reset_index()
Metodo=Pago['index'].to_list()
Metodo_Cantidad=Pago["Metodo de Pago"].to_list()
plt.pie(Metodo_Cantidad,labels=Metodo,autopct='%1.1f%%')
plt.title('Metodo principal de compras')
plt.show()
#################################################################
print("")
print("")
print("ANALISIS POR CLIENTES")
Clientes=Excel.copy()
Clientes=Clientes["Cliente"].value_counts().to_frame().reset_index()
MejoresClientes=Clientes.head(3)
print("El mejor cliente es:",MejoresClientes.iloc[0,0],"con",MejoresClientes.iloc[0,1],"compras")
print("")
print("Esta es la lsita de los mejores 3 clientes")
print(MejoresClientes)
print("")
print("")
###################################ANALISIS POR PRODUCTOS################################
Clientes=Excel.copy()
Mejores_Productos=Clientes[["Producto","Cantidad"]]
Productos=Mejores_Productos["Producto"].unique().tolist()
Productos_Conteo=pd.DataFrame({"Producto":[],"Cantidad Total":[]})
for i in Productos:
    Data=Mejores_Productos[Mejores_Productos["Producto"]==i]
    Cantidad=Data["Cantidad"].sum()
    Data=pd.DataFrame({"Producto":[i],"Cantidad Total":[Cantidad]})
    Productos_Conteo=pd.concat([Productos_Conteo,Data],ignore_index=True)
Productos_Conteo=Productos_Conteo.sort_values(by="Cantidad Total",ascending=False)
Total_Productos=Productos_Conteo["Cantidad Total"].sum()
Top5=Productos_Conteo.head(9)
CantidadTop5=Top5["Cantidad Total"].sum()
Cantidad_Otros=Total_Productos-CantidadTop5
Otros=pd.DataFrame({"Producto":["Otros"],"Cantidad Total":[Cantidad_Otros]})
Top5=pd.concat([Top5,Otros],ignore_index=True)
print("La lista de productos con mayor venta son:")
print(Top5)
plt.figure(2)
plt.bar(Top5["Producto"].tolist(),Top5["Cantidad Total"].tolist())
plt.xticks(fontsize=7)
plt.xlabel("Producto")
plt.ylabel('Cantidad Comprada')
plt.title("Productos mas comprados")
plt.show()
print("")
print("")
########################PRODUCTOS CON MAYOR GANANCIA####################
Clientes=Excel.copy()
Ganancias_Productos=Clientes[["Producto","Costo total"]]
Productos_Ganancias=Ganancias_Productos["Producto"].unique().tolist()
Ganancia_Conteo=pd.DataFrame({"Producto":[],"Ganancia":[]})
for j in Productos_Ganancias:
    Data=Ganancias_Productos[Ganancias_Productos["Producto"]==j]
    Ganancia=Data["Costo total"].sum()
    Data=pd.DataFrame({"Producto":[j],"Ganancia":[Ganancia]})
    Ganancia_Conteo=pd.concat([Ganancia_Conteo,Data],ignore_index=True)
Ganancia_Conteo=Ganancia_Conteo.sort_values(by="Ganancia",ascending=False)
Ganancias_Total=Ganancia_Conteo["Ganancia"].sum()
GananciasTop10=Ganancia_Conteo.head(10)
Total_Ganancia10=GananciasTop10["Ganancia"].sum()
Ganancia_Otros=Ganancias_Total-Total_Ganancia10
DF_GanaciasOtros=pd.DataFrame({"Producto":["Otros"],"Ganancia":[Ganancia_Otros]})
GananciasTop10=pd.concat([GananciasTop10,DF_GanaciasOtros],ignore_index=True)
print("Los productos que representan mayor ganancia son:")
print(GananciasTop10)
plt.figure(3)
plt.bar(GananciasTop10["Producto"].to_list(),GananciasTop10["Ganancia"].to_list())
plt.xticks(fontsize=7)
plt.xlabel("Producto")
plt.ylabel("Ganancia generada")
plt.title("Ganancia por cada producto")
plt.show()
################ ANALISIS GENERO DE CLIENTES##############
Clientes=Excel_Clientes.copy()
Genero=Clientes["Genero"]
Genero=Genero.value_counts().to_frame().reset_index()
print("Genero de nuestros clientes:")
print(Genero)
print("")
print("")
plt.figure(4)
plt.pie(Genero["Genero"].to_list(),labels=Genero["index"].to_list(),autopct='%1.1f%%')
plt.title("Genero de clientes")
plt.show()
############### PRODUCTOS NO COMPRADOS############
NoComprados=pd.read_excel('Productos.xlsx')
NoComprados=NoComprados["PRODUCTO"].to_list()
Comprados=Excel.copy()
Comprados=Comprados["Producto"].unique().tolist()
Faltantes=list(set(NoComprados)-set(Comprados))
print("Se presenta una lista de los productos que no se han comprado")
print(Faltantes)

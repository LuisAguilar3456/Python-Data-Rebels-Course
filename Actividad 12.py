import pandas as pd
print("Los datos son:")
print("")
salarios={
    "Nombre":["Ringo","John","Paul","Geroge","Yoko"],
    "Edad":[45,34,42,38,47],
    "Salario":[12000,14000,13000,11000,10000],
    "Genero":["M","M","M","M","F"]
}
Inf=pd.DataFrame.from_dict(salarios)
print(Inf)
print("")
Maximo=Inf["Salario"].max()
print("El salario maximo es:",Maximo)
print("")
Minimo=Inf["Salario"].min()
Mediana=Inf["Salario"].median()
print("El salario minimo es:",Minimo)
print("")
print("El rango es:",Maximo-Minimo)
print("")
print("")
Data=Inf["Salario"].describe()
print("Hay",Data[0],"datos")
print("El promedio es:",Data[1])
print("La desviación estandar es:",Data[2])
print("La Mediana es:",Mediana)
print("El 25 de los datos es:",Data[4])
print("El 50 de los datos es:",Data[5])
print("El 75 de los datos es:",Data[6])
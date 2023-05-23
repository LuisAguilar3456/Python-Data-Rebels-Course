import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Excel=pd.read_csv("cleanstudentscomplete.csv")
Excel_Cate=Excel.copy()
Lectura=Excel["reading_score"].to_list()
Mate=Excel["math_score"].to_list()
Lectura_Cate=list()
Mate_Cate=list()
for x in Lectura:
    if x>=70:
        Lectura_Cate.append("Aprobado")
    else:
        Lectura_Cate.append("No aprobado")
for y in Mate:
    if y>=70:
        Mate_Cate.append("Aprobado")
    else:
        Mate_Cate.append("No aprobado")
Excel_Cate["cat_read"]=Lectura_Cate
Excel_Cate["cat_math"]=Mate_Cate
print("Tabla original con las variables categoricas:")
print("")
print("")
print(Excel_Cate.head())
Lectura=Excel_Cate.value_counts(subset='cat_read').to_frame().reset_index()
Mate=Excel_Cate.value_counts(subset='cat_math').to_frame().reset_index()
Aprobados=Lectura['cat_read'].to_list()
Lectura=Lectura[0].to_list()
Mate=Mate[0].to_list()
plt.figure(1)
plt.pie(Lectura,labels=Aprobados,autopct='%1.1f%%')
plt.title("# de estudiantes aprobados en Lectura")
plt.savefig("AprobadoLectura.png")
plt.show()
plt.figure(2)
plt.pie(Mate,labels=Aprobados,autopct='%1.1f%%')
plt.title("# de estudiantes aprobado en Mate")
plt.savefig("AprobadosMate.png")
plt.show()
###########################Division Mujeres vs Hombres#####################
Hombres=Excel_Cate.copy()
Mujeres=Excel_Cate.copy()
Hombres=Hombres[Hombres["gender"]=="M"]
LectH=Hombres.value_counts(subset="cat_read").to_frame().reset_index()
LectH=LectH[0].to_list()
MateH=Hombres.value_counts(subset="cat_math").to_frame().reset_index()
MateH=MateH[0].to_list()
Mujeres=Mujeres[Mujeres["gender"]=="F"]
LectM=Mujeres.value_counts(subset="cat_read").to_frame().reset_index()
LectM=LectM[0].to_list()
MateM=Mujeres.value_counts(subset="cat_math").to_frame().reset_index()
MateM=MateM[0].to_list()
Lectura=pd.DataFrame({"Aprobados":Aprobados,"Hombres":LectH,"Mujeres":LectM})
Matematicas=pd.DataFrame({"Aprobados":Aprobados,"Hombres":MateH,"Mujeres":MateM})
print("# de Hombes vs Mujeres Aprobados en Lectura")
print(Lectura)
Lectura.plot(x="Aprobados",y=["Hombres","Mujeres"],kind="bar",title="# Niños vs Niñas aprobados en Lectura")
plt.show()
print("")
print("")
print("# de Hombres vs Mujesres Aprobados en Matematicas")
print(Matematicas)
Matematicas.plot(x="Aprobados",y=["Hombres","Mujeres"],kind="bar",title="# Niños vs Niñas aprobados en Matematicas")
plt.show()
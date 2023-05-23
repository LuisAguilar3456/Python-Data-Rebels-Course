import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Excel=pd.read_csv("cleanstudentscomplete.csv")
################# 10% MEJORES EN LECTURA #########################
Quantile_90=Excel.copy()
Quant=Quantile_90["reading_score"].quantile(0.9)
Quantile_90=Quantile_90[Quantile_90["reading_score"]>=Quant]
Quant90_Ninos=Quantile_90[Quantile_90["gender"]=="M"]
Quant90_Ninas=Quantile_90[Quantile_90["gender"]=="F"]
ReadM=Quant90_Ninos["reading_score"].mean().__round__(3)
CReadM=Quant90_Ninos.shape[0]
ReadF=Quant90_Ninas["reading_score"].mean().__round__(3)
CReadF=Quant90_Ninas.shape[0]
print("LOS MEJORES 10 EN LECTURA")
print("Los mejores",CReadM,"hombres tienen un promedio de",ReadM,"en lectura")
print("Las mejores",CReadF,"mujeres tienen un promedio de",ReadF,"en lectura")
print("")
print("")
############## 10% PEORES EN LECTURA ############################
Quantile_10=Excel.copy()
Quant=Quantile_10["reading_score"].quantile(0.1)
Quantile_10=Quantile_10[Quantile_10["reading_score"]<=Quant]
Quant10_Ninos=Quantile_10[Quantile_10["gender"]=="M"]
Quant10_Ninas=Quantile_10[Quantile_10["gender"]=="F"]
ReadM=Quant10_Ninos["reading_score"].mean().__round__(3)
CReadM=Quant10_Ninos.shape[0]
ReadF=Quant10_Ninas["reading_score"].mean().__round__(3)
CReadF=Quant10_Ninas.shape[0]
print("LOS PEORES 10 EN LECTURA")
print("Los peores",CReadM,"hombres tienen un promedio de",ReadM,"en lectura")
print("Las peores",CReadF,"mujeres tienen un promedio de",ReadF,"en lectura")
print("")
print("")
############## 10% PEORES EN MATEMATICAS ####################
Quant_MateLect=Quantile_10[['reading_score','math_score']]
print("La Matriz de correlación entre las calificaciones de lectura y matematicas")
print(Quant_MateLect.corr(method="pearson"))
plt.plot(Quant_MateLect["reading_score"],Quant_MateLect["math_score"],'bo')
plt.show()
print("No existe correlación alguna entre estas variables")

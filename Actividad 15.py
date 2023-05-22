import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Excel=pd.read_csv("cleanstudentscomplete-1.csv")
Ninos=Excel.copy()
Ninas=Excel.copy()
Ninos=Ninos[Ninos["gender"]=="M"]
Ninas=Ninas[Ninas["gender"]=="F"]
Grados=Ninos["grade"].unique()
Grados=['9th','10th','11th','12th']
NinosxGrado=Ninos.value_counts(subset="grade").to_frame().reset_index()
NinasxGrado=Ninas.value_counts(subset="grade").to_frame().reset_index()
NumNinos=NinosxGrado[0].to_list()
NumNinas=NinasxGrado[0].to_list()
Ninos=pd.DataFrame({'Grado':Grados,'Niños':NumNinos,'Niñas':NumNinas})
print(Ninos)
Ninos.plot(x="Grado",y=["Niños","Niñas"],kind="bar",title="# de Niños y Niñas por Grado")
plt.savefig("NinosxGrado.png")
plt.show()
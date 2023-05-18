import pandas as pd
import numpy as np 
Excel=pd.read_csv("athlete_events.csv")
print(Excel.head(5))
print("")
Medallas=Excel.set_index("Medal",inplace=False) #Agregar Index por medallas para filtrar 
print(Medallas.info())
print("")
print("")
###############################MEDALLAS DE ORO################################
Oro=Medallas.loc["Gold"] #Filtrar medallas de Oro
OroMayor=Oro[Oro["Age"]==np.max(Oro["Age"])]
OroMayor=OroMayor.reset_index()
OroMenor=Oro[Oro["Age"]==np.min(Oro["Age"])]
OroMenor=OroMenor.reset_index()
print("Las personas que han obtenido La medalla de Oro con mayor edad son:")
print(OroMayor.iloc[:,[2,4]])
print("Las personas que han obtenido La medalla de Oro con menor edad son:")
print(OroMenor.iloc[:,[2,4]])
print("")
print("")
##########################MEDALLAS DE PLATA########################################
Plata=Medallas.loc["Silver"] #Filtrar medallas de Plata 
PlataMayor=Plata[Plata["Age"]==np.max(Plata["Age"])]
PlataMayor=PlataMayor.reset_index()
print("Las personas que han obtenido La medalla de Plata con mayor edad son:")
print(PlataMayor.iloc[:,[2,4]])
print("")
print("")
#########################MEDALLAS DE BRONCE####################################
Bronce=Medallas.loc["Bronze"] #Filtrar medallas de Bronce
BronceMayor=Bronce[Bronce["Age"]==np.max(Bronce["Age"])]
BronceMayor=BronceMayor.reset_index()
print("Las personas que han obtenido La medalla de Bronce con mayor edad son:")
print(BronceMayor.iloc[:,[2,4]],type(BronceMayor))
print("")
print("")
#######################BORRAR LOS QUE NO TENGAN MEDALLA##########################
ConMedalla=Excel.copy()
print(ConMedalla.isnull().sum())
ConMedalla=ConMedalla.dropna(subset="Medal")
MasMedallas=ConMedalla["Name"].value_counts()
MasMedallas=MasMedallas.to_frame()
MasMedallas=MasMedallas.reset_index()
print("Los competidores mas ganadores son:")
print("")
print(MasMedallas.head(5))
print("")
print("")
MasGanador=Excel.copy()
MasGanador=MasGanador[MasGanador["Name"]==MasMedallas.iloc[0,0]]
print("Estas son las estadisticas del deportista mas ganador:")
print(MasGanador,type(MasGanador))
MasGanador.to_excel(r'\Users\dell\Documents\Python Data Rebels\Python-Data-Rebels-Course\MasGanador.xlsx', index=False)


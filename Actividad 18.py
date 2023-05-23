import numpy as np
y=list()
for x in range(3,22):
    y.append(x)
Ar=np.array(y)
print(Ar,type(Ar))
print("")
print("")
Ar2=np.array([0,1,2,3,4,0,1,2,3,4])
print(Ar2,type(Ar2))
print("")
print("")
Asc=np.sort(Ar2)
print(Asc,type(Ar2))

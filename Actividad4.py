x,y=24,6 #2x=24, #1/3y-15=6
x//=2 #x=24/2
y+=15 #1/3y=6+15
y*=3 #y=(6+15)*3
print("Yo tengo",x,"de edad")
print("Mi hermana tiene",y,"de edad")
if x>y:
    print("Yo soy mas grande que mi hermana, yo tengo",x,"años y ella",y,"años")
elif y>x:
    print("Mi hermana es mams grande que yo, ella tiene",y,"años y yo",x,"años de edad")
else:
    print("Mi hermana y yo tenemos la misma edad")
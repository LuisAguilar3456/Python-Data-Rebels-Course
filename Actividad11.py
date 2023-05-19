import numpy as np
class calculadora():
    def __init__(self,num1,num2):
        self.num1=float(num1)
        self.num2=float(num2)
    def sumar(self):
        suma=self.num1+self.num2
        print("El resultado de la suma es:",suma)
    def restar(self):
        resta=self.num1-self.num2
        print("El resultado de la resta es:",resta)
    def multiplicar(self):
        multiplicacion=self.num1*self.num2
        print("El resultado de la multiplicación es:",multiplicacion)
    def dividir(self):
        division=self.num1/self.num2
        print("El resultado de la división es:",division)
        
class calculadoraAvanzada(calculadora):
    def elevar(self):
        elevado=self.num1**self.num2
        print("El resultado de la potencia es: ",elevado)
    def raiz(self):
        raiz1=self.num1**(0.5)
        raiz2=self.num2**(0.5)
        print("Las raices cuadradas son:",raiz1,raiz2)


num1=input("Ingrese un número: ")
num2=input("Ingrese un número: ")
print("Calculadora normal:")
print("")
calculador=calculadora(num1,num2)
calculador.sumar()
calculador.restar()
calculador.multiplicar()
calculador.dividir()
print("")
print("")
print("Calculadora Avanzada:")
print("")
calculador2=calculadoraAvanzada(num1,num2)
calculador2.elevar()
calculador2.raiz()
calculador2.sumar()
# print("introduzca el radio")
# radio=int(input())
# PI=3.14
# area=(radio * radio) * PI
# print("el area del circulo es " , area)

def calcular_area(num):
    area=(num*num)*3,14
    return area

print("ingrese un numero")
num=int(input())
print(calcular_area(num))

def calcular_perimetro(num):
    perimetro =(num)*4
    return perimetro

print ("ingrese un numero")
num=int(input())
print(calcular_perimetro(num))

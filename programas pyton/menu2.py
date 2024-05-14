def multiPorDos():

    print("Ingrese un numero")
    num=int(input())
    print(num*2)

def resta5():
    print("Ingrese un numero")
    num=int(input())
    print(num-5)

def validaFolio():
    ticket_valido=False
    folio_valido=123
    print("Ingrese el numero de folio")
    n_folio=int(input())

    if n_folio==folio_valido:
        ticket_valido=True

def suma(num1, num2):
    resul=num1+num2
    return resul
def resta(num1, num2):
    resul=num1-num2
    return resul
def multi(num1, num2):
    resul=num1*num2
    return resul
def divi(num1, num2):
    resul=num1/num2
    return resul 
def Perimetrocuadrado(num):
    Result=num*4
    return Result
def Areacirculo(num):
    result=num*4
    return result
def calcular_area(num):
    area=(num*num)* 3.14
    return area
def area_cuadrado(num):
    area=(num*num )
    return area 
def area_triangulo(num, num2):
    area=(num*num2)/2
    return area 
def area_rectangulo(b, a):
    area=(b*a)
    return area 
def Tpitagoras(cateto1, cateto2):
   hipotenusa= ((cateto1**2)+(cateto2**2))
   return(hipotenusa )
    




while True:
    print("Seleccione una opcion")
    print("1.- -Suma")
    print("2.- -Resta")
    print("3.- -Multiplicacion")
    print("4.- -Division")
    print("5.- -Perimetro del cuadrado")
    print("6.- -area del circulo")
    print("7.- -area del cuadrardo")
    print("8.- -area de un triangulo")
    print("9.- -area de un rectangulo")
    print("10.- -pitagoras")
    op=int(input())
    while True:
        match op:
           case 1:
            print("Ingrese 2 numeros")
            num1=int(input())
            num2=int(input())
            print("Su resultado es ",suma(num1,num2))
           case 2:
            print("Ingrese 2 numeros")
            num1=int(input())
            num2=int(input())
            print("Su resultado es ",resta(num1,num2))
           case 3:
            print("Ingrese 2 numeros")
            num1=int(input())
            num2=int(input())
            print("Su resultado es ",multi(num1,num2))
           case 4:
            print("Ingrese 2 numeros")
            num1=int(input())
            num2=int(input())
            print("Su resultado es ",divi(num1,num2))
           case 5:
            print("Ingrese 1 numero")
            l=int(input())
            print("Su resultado es ",Perimetrocuadrado(l))
           case 6:
            print("ingrese un numero")
            num=int(input())
            print("Su resultado es", calcular_area(num))
           case 7:
            print("ingrese un  numero")
            num=int(input())
            print( "Su resultado es", area_cuadrado(num))
           case 8:
            print("ingrese dos numero")
            num=int(input())
            num2=int(input())
            print( "Su resultado es", area_triangulo(num, num2))
           case 9:
            print("ingrese dos numero")
            b=int(input())
            a=int(input())
            print( "Su resultado es", area_rectangulo(b, a))
           case 10:
            print("ingrese los catetos")
            b=int(input())
            c=int(input())
            print( "Su resultado de la hipotenusa es" , Tpitagoras(b, c))
            break
  
    


# num1=int(input())
# num2=int(input())
# while num2==0:
#     print("Elija un numero distinto a cero")
#     num2=int(input())
    
# print(divi(num1,num2)
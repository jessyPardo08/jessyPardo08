print("Seleccione una opccion")
print("1. - -suma")
print("2. - - resta")
print("3. - - multi")
print("4. - -divi")
print("4. - -area")
print("4. - -perimetro")

op=int(input())

match op:
    case 1:
        print("ingrese dos numeros")
        num1=int(input())
        num2=int(input())
        print(num1+num2)
        resul= num1+num2
        print("su resultado es", (num1, num2))

    case 2:
         print("ingrese dos numeros")
         num1=int(input())
         num2=int(input())
         print(num1-num2)
         resul= num1-num2
         print("su resultado es",(num1, num2))
    
    case 3:
        print("ingrese dos numeros")
        num1=int(input())
        num2=int(input())
        print(num1*num2)
        resul= num1*num2
        print("su resultado es",(num1 , num2))
   
    case 4:
        print("ingrese dos numeros")
        num1=int(input())
        num2=int(input())
        print(num1/num2)
        resul= num1/num2
        print("su resultado es",(num1, num2))
    
    case 5:
       def calcular_area(num):
        area=(num*num)*3,14
        return area

        print("ingrese un numero")
        num=int(input())
        print(calcular_area(num))
    
    case 6:
        def calcular_perimetro(num):
         perimetro =(num)*4
         return perimetro

         print ("ingrese un numero")
         num=int(input())
         print(calcular_perimetro(num))
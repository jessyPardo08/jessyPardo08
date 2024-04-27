print("Seleccione una opccion")
print("1. - -suma")
print("2. - - resta")
print("3. - - multi")
print("4. - -divi")
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
        print("su resultado es",(num1, num2))
   
    case 4:
        print("ingrese dos numeros")
        num1=int(input())
        num2=int(input())
        print(num1/num2)
        resul= num1/num2
        print("su resultado es",(num1, num2))

        
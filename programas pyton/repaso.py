print("ingrese su nombre ")
nombre_de_usuario=(input())
while True:
   print("seleccione una carrera")
   print("carrera 1 ")
   print("carrera 2 ")
   print("carrera 3 ")
   op=int(input())

   match op:  
    case 1 : 
        print(nombre_de_usuario)
        semestres=int(8)
        print (" Esta carrera dura 8 semestres")
        valor_mesual=int(300000)
        print("El valor mesual es de ", valor_mesual)
        valor_anual=int(valor_mesual * 2)
        print (" El valor anual es de ", valor_anual)
        valor_total=int(300000 * 8 )
        print(" El valor total es de " , valor_total)
        if  semestres > 6 : 
         print(" Ya que la carrera consta con mas de 6 semestres" )
         print(" Usted tiene un descuento de 15%, al valor total de la carrera")
         quince_por_ciento = valor_total * 0.15 
         print("El descuento es de ", quince_por_ciento )
        else:
         semestres  < 6 
         print("Esta carrera no tiene descuento")
        
        

    case 2:
       print(nombre_de_usuario)
       semestres=int(6)
       print ("esta carrera dura 6 semestres " )
       valor_mesual=int(300000)
       print("su valor mesual es de ", valor_mesual)
       valor_anual=int(valor_mesual * 2)
       print ("su valor anual es de ", valor_anual)
       valor_total=int(300000 * 6 )
       print("su valor totla es de " , valor_total)
       if  semestres > 6 : 
        print(" Ya que la carrera consta con mas de 6 semestres" )
        print(" Usted tiene un descuento de 15%, al valor total de la carrera")
        quince_por_ciento = valor_total * 0.15 
        print("El descuento es de ", quince_por_ciento )
       else:
        semestres  < 6 
        print("Esta carrera no tiene descuento")
       
   
    case 3: 
       print(nombre_de_usuario)
       semestres=int(10)
       print ("esta carrera dura 10 semestres")
       valor_mesual=int(300000)
       print("su valor mensual es de ", valor_mesual)
       valor_anual=int(valor_mesual * 2)
       print ("su valor anual es de ", valor_anual)
       valor_total=int(300000 * 10 )
       print("su valor total es de " , valor_total)
       if  semestres > 6 : 
        print(" Ya que la carrera consta con mas de 6 semestres" )
        print(" Usted tiene un descuento de 15%, al valor total de la carrera")
        quince_por_ciento = valor_total * 0.15 
        print("El descuento es de ", quince_por_ciento )
       else:
        semestres  < 6 
        print("Esta carrera no tiene descuento")
   
    case 4 :
       print(" salir del menu")
       break 
   
    case _:
       ("invalido")
       







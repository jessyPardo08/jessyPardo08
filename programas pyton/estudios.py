print("ingrse el nombre del cliente")
nombre=input()
while True:  
 menu={
  "arroz ala francesa":4500,
  "arroz marinero":5200,
  "sopa marinera":9700
 }
  
 print("Elija un menu")
 print("menu 1 ")
 print("menu 2 ")
 print("menu 3 ")

 op=int(input())
 

 match op:
  case 1 :
   print( )
   
    
   
  case 2: 
   print( )
      
      
  case 3:
   print( )
       
  case 4:
   print("no quiero comer mas, me traes la cuenta ")
   break
  case _:
   print("Opcion invalida , porfavor selecccione una opccion valida")



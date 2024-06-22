while True:
 
 op= 
 match op:
     case 1:
      print("en que piso se va a alojar ")
      piso=int (input())
      print("en que habitacion se va alojar")
      hab=int(input())
      if hotel [piso-1][hab-1]:
        print("la habitacion esta usada")
      else:
        nom=input("ingrese un nombre\n")
     hotel[piso-1][hab-1]={"nombre":nom}
     
     case 2:
      print("que habiatacion va a actualizar")
      piso=int(input())
      print("que habiatacon a a actualizar")
      hotel[piso-1][hab-1]
    
     case 3:
      for i in hotel:
        print(i)
     case 4:
      f= open("outfile.txt", "w")
      for piso in hotel:
      for hab in hoel:
         
      with open ('archivo de texto')
     case 5:
      break 
     case _:
      print("opcion invalida")
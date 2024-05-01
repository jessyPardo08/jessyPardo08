# print("ingrese su nombre ")
# nombre_de_usuario =input()
# print("ingrese su apellido ")
# apellido_de_usuario =input()
# print( nombre_de_usuario + apellido_de_usuario  + " este es su primer programa ")

# print ("porfavor ingresa un numero")
# num=int(input())
# print ("porfavor ingresa un numero")
# num2=int(input())
# print ("porfavor ingresa un numero")
# num3=int(input())


# if num>num2 and num2>num3:
#     print(" El " + str (num) + " es mayor que todos ")
# elif num2>num3:
#     print(" El " + str (num2) + " es mayor que todos " )
# else:
#     print(" El " + str (num3) + " es mayor que todos ")

def validar_ticket (numero_ticket):
  if 100< numero_ticket<750:
     print ("ticket valido ")

def determinar_sector(numero_ticket):
    if 100 <numero_ticket <400:
        print("cancha") 
    elif 401 <numero_ticket <750:
       print("galeria") 
    else:
        return ("ticket fuera de rango")
 




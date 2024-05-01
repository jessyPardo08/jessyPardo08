# for i in range (10):
#     print (i)


# lista_numeros = {1,2,3,4,5,6,7,8}
# for valor in lista_numeros:
#  if   valor > 3:

#   print("este valor es", valor, "es mayor que 3") 

print("ingrese numero de ticket") 
numero_de_ticket_valido=int(input())

if numero_de_ticket_valido > 100 and numero_de_ticket_valido <750:
    print ("su numero de ticket es valido")
    print (" segun su numero de ticket ")

if numero_de_ticket_valido >= 100 and numero_de_ticket_valido <=350:
    print (" usted va a cancha ")
elif numero_de_ticket_valido >=351 and numero_de_ticket_valido <=750:
    print(" usted va a galeria ")
else:
    print(" usted no puede entrar ")


# #numero random
import random
# num=random.randint(0,100)
# num2=random.randint(0,100)
# lista=[41,73,4,55,77,89]
# ##agregar a la lista 
# lista.append(num)
# lista.append(num2)

# ##imprime todos los elementos
# for elemento in lista:
#     print(elemento)

# ##imprime un elemento
# print(lista[2]) 

##suma de elementos 
# print(lista[2]+ lista[4])

bingo=[45,17,24,46,90]
comodin=random.randint(10, 99)

while comodin in bingo:
    # print("creando nuevo comodin")
    comodin=random.randint(10, 99)
bingo.append(comodin)


for num in bingo:
    print(num)
   
# def funcion_sencilla():
#     print("Hola, soy una funcion sencilla")





# funcion_sencilla()

# # def MuestraPorPantalla(palabra):
# #     print(palabra)

# # palabra="algo"
# # MuestraPorPantalla(palabra)
#calculadora

# def suma(a,b):
#     sumar = a + b
#     return(sumar)
    
# num1 = int(input("Ingrese primer número: "))
# num2 = int(input("Ingrese segundo número: "))
# print(f"La suma es: ",suma(num1,num2))
 


# def recorrer_lista(lista):
#  for elemento in lista:
#   print(elemento)

# mi_lista=[1,2,3,4]
# # recorrer_lista(mi_lista)

# def separarNumParesDeImpares(lista):
#  pares=[]
#  impares=[]

#  for numero in lista:
#   if numero % 2 ==0:
#    pares.append(numero)
#   else:
#    impares.append(numero)
#  return pares, impares
# pares, impares= separarNumParesDeImpares(mi_lista)
# print("numeros pares:" , pares)
# print("numeros impares:", impares)


# def buscar_valor(diccionario, key):
#  if key in diccionario:
#   return diccionario[key]
#  else:
#   return f"la clave '{key}' no existe en el diccionario"
# mi_diccionario={'a':1, 'b': 2, 'c':3}

# clave_buscada= str(input("ingrese numero indice"))

# resultado=buscar_valor(mi_diccionario, clave_buscada)

# print(resultado)

# def crear_diccionario():
#  diccionario={}
#   key=input("ingrese una key")
#   value=input("ingrese el  valor de la key annterior")
#   diccionario=[key]=value
#   print(diccionario)

# crear_diccionario()

def crear_diccionario():
    diccionario={}
    
    while True:
        key=input("ingrese una key")
        if key.lower()== "shazam":
         print(diccionario)
         break
        else:
          value=input("ingrese el  valor de la key anterior '{key}' :")
          diccionario= [key] = value
          print(diccionario)


crear_diccionario()
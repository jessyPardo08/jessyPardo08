# def funcion_sencilla():
#     print("Hola, soy una funcion sencilla")





# funcion_sencilla()

# # def MuestraPorPantalla(palabra):
# #     print(palabra)

# # palabra="algo"
# # MuestraPorPantalla(palabra)
# #calculadora
# def sumar(a, b):
#     return a + b

# def restar(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     if b == 0:
#         return "Error: No se puede dividir por cero."
#     else:
#         return a / b

# def validar_num(numero_entrada):
#     while True:
#         try:
#             numero = float(input(numero_entrada))
#             return numero
#         except ValueError:
#             print("Error: Ingrese un valor numérico válido.")

# # Ingreso de dos números con validaciones
# num1 = validar_num("Ingrese el primer número: ")
# num2 = validar_num("Ingrese el segundo número: ")

# resultado_suma = sumar(num1, num2)
# resultado_resta = restar(num1, num2)
# resultado_multiplicacion = multiplicar(num1, num2)
# resultado_division = dividir(num1, num2)

# print(f"Suma: {resultado_suma}")
# print(f"Resta: {resultado_resta}")
# print(f"Multiplicación: {resultado_multiplicacion}")
# print(f"División: {resultado_division}")

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

def crear_diccionario():
 diccionario={}
 while True:
  key=input("ingrese plabra clave para salir")
   
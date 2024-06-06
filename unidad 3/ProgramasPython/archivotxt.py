#Las comillas al inicio y 3 al final del texto representan un texto
#con saltos de línea
# datos = """Este es un archivo de texto simple que no tiene 
# ningún formato en particular, lo podemos utilizar
# para guardar todo tipo de texto. 
# """
# with open('archivo.txt', 'w') as archivo:
#     archivo.write(datos)


# # Opción 1
# # Sintaxis: open('nombre_del_archivo', 'modo')
# # Modos comunes: 'r' (lectura), 'w' (escritura), 'a' (anexar), 'r+' (lectura/escritura)
# archivo = open('datos.txt', 'r')
# contenido = archivo.read()
# print(contenido)
# archivo.close()

# # Opción 2
# # Usando el contexto 'with', el archivo se cierra automáticamente al salir del bloque 'with'
# with open('datos.txt', 'r') as archivo:
#     contenido = archivo.read()
#     print(contenido)


# Abrir archivo, r es permiso de lectura
# with open('datos.txt', 'r') as archivo:
#     contenido = archivo.read()
# print(contenido)

# num=int(input())

# with open('archivo33.txt', 'w')as archivo:
#  for i in range(1,11):
#     archivo.write(str(num) + " x " + str(i) +" = " +str(num*i) '\n')
# #  print(num, " x ", i , "=", num*i)

n=int(input("ingrese el primer numero"))
n2=int(input("ingrese el segundo numero"))
nombre_fichero= 'tabla' + str(n) + str(n2) + '.txt'
with open(nombre_fichero, 'w') as f:
    f.write(str(n) + '+' + str(n2) '=' + str(num1+num2))
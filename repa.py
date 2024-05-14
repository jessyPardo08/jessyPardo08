saldo=10000

while True:
    print("este es el menu ")
    print("1 ingresa al menu 1")
    print("2 ingresa al menu 2 ")
    print("3 salir")
    
    op=int(input("ingrese una opccion"))

    match op:
        case 1 :
            print ("tu sueldo actual ", saldo)
        case 2: 
            retirar=int(input("cuanto retiramos"))
            if saldo>=retirar:
                print ("ingresaste 2 ")
                saldo=retirar
                #saldo=saldo-retirar
        case 3:
            print ("adios")    
            break
        case _:
            ("ingrese otra cosa")


# for i in ("hola como estas"):
#     print(i)

# for i in range(1, 7):
#     print(i)

# frase="hola como estas"
# cont=0
# for i in range

# for i in range(len(frase)):
#     cont+=1
#     print(i)
#     print("la frase tenia", cont, "letras")
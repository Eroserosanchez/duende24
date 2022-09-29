contador = 0
valor = 0
minimo = 0
maximo = 0
primerNumero = True
while True:
    numero = input ("Ingrese un número: ")
    if(numero == "salir"):
        break
    else:
        valor=valor+int(numero)
        contador=contador+1
    if (primerNumero):
        minimo = int(numero)
        maximo= minimo
        primerNumero= False
    else:
        if (int(numero)>maximo):
            maximo = int(numero)
        if(int(numero)<minimo):
            minimo = int(numero)
print ("Máximo", maximo)
print ("Mínimo", minimo)
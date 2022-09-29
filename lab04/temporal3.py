from operator  import truediv


contador = 0
suma = 0
primernumero = True
while True:
    try:
        numero = input("ingrese un numero:")
        if(numero == "fin"):
           break
        contador = contador + 1
        suma = suma + int(numero)

    except:
        print ("Dato erroneo")


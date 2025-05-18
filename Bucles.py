

"""

notas=int(input("Ingrese la Cantidad de Notas: "))

resultado = 0


for i in range (notas):

    valor_nota= int(input("Ingrese la nota Obtenida: "))
    
    resultado = resultado + valor_nota

promedio = resultado / notas

print (f"El Promedio Obtenido de las Notas es {promedio}")


"""

# Obtencion de Numero Primo e impresion de los Mismos de 1 a 21

"""


for num in range (2,21):

    primo = 1

    for div in range (2,num):

        if (num % div) == 0:

            primo = 0
    
    if primo == 1:

        print (f"{num} ", end="")

print ("\n")

    
"""

for i in range (2,21):

    print(f"Esta es la Impresion {i}")

    print ("Chau a Todos")

    print ("Hola")
    
    print ("Hola Mundo")

    print("Pude hace que funcionara la Sincronizacion con Git HUB")






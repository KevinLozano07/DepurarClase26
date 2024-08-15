#Modifica el código para que, si la lista está vacía, devuelva un mensaje que diga "La lista está vacía" en lugar de intentar calcular el promedio.

def calcular_promedio(numeros):

    suma = 0     
    for numero in numeros:
     suma += numero
     
    promedio = suma / len(numeros)
    return promedio

lista_numeros = []

if lista_numeros == []:
 print("")
 print("La lista esta vacia")
 print("")
else:
 print("")
 print("El promedio es:", calcular_promedio(lista_numeros))
 print("")
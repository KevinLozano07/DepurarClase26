#Modifica el código para que funcione con cualquier lista, incluyendo listas con solo números negativos.

def encontrar_maximo(numeros):

    maximo = numeros[0]

    for numero in numeros:

        if numero > maximo:

            maximo = numero

    return maximo



lista_numeros = [-10, -20, -30, -5, -15]

print("")
print("El valor máximo es:", encontrar_maximo (lista_numeros))
print("")
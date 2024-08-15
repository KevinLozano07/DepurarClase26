def filtrar_pares(numeros):

    pares = []
    
    if 0 in numeros:
        pares.append(0)
        
        
    for numero in numeros:
        
        if numero % 2 == 0 and numero != 0:

            pares.append(numero)

    return pares



lista_numeros = [-10, -2, 0, 1, 2, 3, 4, 5, 6]

print("")
print("Números pares:", filtrar_pares(lista_numeros))
print("")
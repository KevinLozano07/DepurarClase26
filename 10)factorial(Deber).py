# Asegúrate de que el código funcione correctamente para calcular el factorial de cualquier número entero positivo.

def factorial(n):

    resultado = 1

    for i in range(1, n + 1):

        resultado *= i

    return resultado



numero = 1 #El factorial de 1 da 1 y el factorial de 0 da 1

print("")
print("Factorial de", numero, "es:", factorial(numero))
print("")
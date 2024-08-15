#Corrige el código para que pueda identificar correctamente si una palabra es un palíndromo.

def es_palindromo(palabra):

    palindroma = palabra[::-1]
    
    if palabra == palindroma:
        return True
    else:
        return False


palabra = "radar"

print("")
print(f"¿La palabra '{palabra}' es un palíndromo? {es_palindromo(palabra)}")
print("")

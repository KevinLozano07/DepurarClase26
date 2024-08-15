#Corrige el código para que invierta correctamente cualquier cadena.

def invertir_cadena(cadena):

    invertida = ""

    for i in range(len(cadena)):

        invertida = cadena[::-1]

    return invertida



cadena = "Python"

print("")
print("Cadena invertida:", invertir_cadena(cadena))
print("")
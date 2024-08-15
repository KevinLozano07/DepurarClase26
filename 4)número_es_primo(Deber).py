#Optimiza el código para que se detenga cuando sea evidente que el número no es primo, en lugar de recorrer todos los números

def es_primo(n):
    
 if n <= 1:
     return False
 
 if n == 2:
     return True
 
 Raiz = int(n ** 0.5) + 1
 
 for i in range(2, Raiz):
     if n % i == 0:
         return False
     
 return True 

numero = 29

print("")
print(f"¿El número {numero} es primo? {es_primo(numero)}")
print("")
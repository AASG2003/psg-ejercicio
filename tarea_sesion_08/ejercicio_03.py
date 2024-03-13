# Ingresa una cadena por teclado y almacena el valor en una tupla
# Concatena la tupla ('¡', ) + tupla almacenada + la tupla ('!', )
# Imprime el resultado concatenado
# Repite la tupla final 3 veces e imprime el nuevo resultado
cadena = input("Ingresa una cadena: ")
tupla = tuple(cadena)
nueva_tupla = ('¡', ) + tupla + ('!', )
print(nueva_tupla)
print(nueva_tupla * 3)


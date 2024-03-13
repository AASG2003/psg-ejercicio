# De la siguiente lista [1,2,3,4,5,6,7,8,9,10] obtener una 
# sublista inversa con los elementos múltiplos de 3
lista = [1,2,3,4,5,6,7,8,9,10]
lista_inversa = [x for x in lista[-1::-1] if x % 3 == 0]
print(lista_inversa)

# Crea una tupla con los siguientes elementos 1,2,3,4,5,6,7,8,9,10 y realiza:
# Imprime el primer elemento
# Imprime el último elemento
# Imprime un slice del 4 al 7
# Imprime un slice del 2 al 9 con pasos de 3
# Imprime un slice del 10 al 1 con saltos de -2

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Primer Elemento: {tupla[0]}")
print(f"Ultimo Elemento: {tupla[len(tupla) - 1]}")
print(f"Slice del 4 al 7: {tupla[4:8:1]}")
print(f"Slice del 2 al 9 con pasos de 3: {tupla[2:10:3]}")
print(f"Slice del 10 al 1: {tupla[10::-2]}")

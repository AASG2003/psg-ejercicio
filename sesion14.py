# def repetir_lista_animales(lista_animales, veces):
#     return lista_animales * veces

# lista = ['🐶','🐱','🐭','🐹','🐰']
# lista_repetida = repetir_lista_animales(lista, 2)
# print(lista_repetida)

# def operacion(num1, num2, operacion):
#     resultado = 0
#     if operacion == "Suma":
#         resultado = num1 + num2
#     elif operacion == "Resta":
#         resultado = num1 - num2
#     elif operacion == "Multiplicacion":
#         resultado = num1 * num2
#     elif operacion == "Division":
#         resultado = num1 / num2
#     return resultado

# print(operacion(9, 3, "Suma"))
# print(operacion(9, 3, "Resta"))
# print(operacion(9, 3, "Multiplicacion"))
# print(operacion(9, 3, "Division"))

# cadena = "python es un lenguaje de programación"
# aeiou_veces = 0
# def proceso_cadena():
#     for ch in cadena:
#         if(ch in "aeiou"):
#             aeiou_veces +=1
#     cadena.title()

# proceso_cadena()
# print(aeiou_veces)
# print(cadena)

def generar_tupla(*objetos):
    return tuple(objetos), list(objetos)


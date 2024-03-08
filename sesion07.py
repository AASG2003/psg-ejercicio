simple = 'Mi cadena permite comillas "dobles" en una sola línea'
doble  = "Mi cadena permite comillas 'simples' en una sola línea"
triple_simple = '''Mi cadena
permite contenido 
en varias líneas y comillas "dobles" '''
triple_doble = """Mi cadena
permite contenido 
en varias líneas y comillas 'simples' """
print (simple)
print (doble)
print (triple_simple)
print (triple_doble)

entero = str(1)
flotante = str(1E-3)
hexadecimal = str(0xA)
booleano = str (True)
print (entero)
print (flotante)
print (hexadecimal)
print (booleano)
print (type(entero))
print (type(flotante))
print (type(hexadecimal))
print (type(booleano))

mensaje = "Hola,\n\teste es un mensaje \vcon algunos caracteres \
especiales como \\ y tabulador."
print(mensaje)

# entrada = input("Ingrese un valor: ")
# print (entrada)
# print (type(entrada))

# entero = int(input("Ingrese un valor entero: "))
# print (entero, type(entero))

# flotante = float(input("Ingrese un valor flotante: "))
# print (flotante, type(flotante))

# booleano = bool(input("Ingrese un valor booleano: "))
# print (booleano, type(booleano))
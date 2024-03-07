# Imprime una tabla de verdad para la siguiente afirmación: 
# "Una puerta tiene dos interruptores que controlan dos luces la puerta sólo 
# debe abrirse cuando las dos luces están apagadas o las dos están encendidas, 
# caso contrario la puerta no se abre, ¿qué operador lógico se puede utilizar?"
a = True
b = True
print (not (a ^ b))
a = False
b = False
print (not (a ^ b))
print("a | b | x")
print("- | - | -")
print("T | T | T")
print("F | F | T")
print("T | F | F")
print("F | T | F")

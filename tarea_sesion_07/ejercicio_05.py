# Escribe un programa que reciba una cadena y retorna verdadero o falso si es palindrome
# la frase o palabra, ejemplo "Anita lava la Tina" es verdad

palabra = input("Ingresa una frase o palabra: ")
palabra = palabra.replace(' ', "").lower();
palabraInv = palabra[len(palabra)-1::-1]
res = palabra == palabraInv
print(res)
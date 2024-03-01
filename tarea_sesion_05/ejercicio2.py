#Escribe un programa en Python que 
#convierta las siguientes temperaturas
#de grados Celsius a grados Fahrenheit:
#30 ºC
#-273.99 ºC
#100 ºC
def grados_celsius_a_fahrenheit(grados_celsius):
    grados_fahrenheit = (grados_celsius * 1.8) + 32
    return grados_fahrenheit

def imprimir_respuesta(grados_celsius):
    grados_fahrenheit = grados_celsius_a_fahrenheit(grados_celsius)
    print(grados_celsius, "ºC son", grados_fahrenheit, "ºF")


imprimir_respuesta(30)
imprimir_respuesta(-273.99)
imprimir_respuesta(100)
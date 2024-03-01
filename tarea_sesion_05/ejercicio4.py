# Calcular el volumen de un cubo donde 
# uno de sus lados mide 10 metros, 
# utilizando la fórmula general del 
# volumen de un cubo

def volumen_cubo(lado):
    volumen = lado ** 3
    return volumen

lado = 10
print("El volumen del cubo de lado {} metros es: {} metros cubicos"
      .format(lado, volumen_cubo(lado)))
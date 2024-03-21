# Anita y Pepito llevan saliendo juntos por 4 semanas, cada vez 
# que salen van a comer a una plaza de comidas. Ambos quieren saber 
# que tan compatibles son viendo cuantos platos de comida tienen 
# en común. A continuación tienes los platos de comida que ambos 
# han ido pidiendo a los largo de sus citas:
# Anita: Sushi, Pizza, Tacos, Hamburguesa, Pasta, Alitas
# Pepito: Pizza, Tacos, Ensalada, Pasta, Helado, Milanesa
# Si la cantidad platos de comida que tienen en comunes mayor a 50% 
# entonces ambos seguirán saliendo
Anita = set({"Sushi,", "Pizza,", "Tacos,", "Hamburguesa,", "Pasta,", "Alitas"})
Pepito = set({"Pizza,", "Tacos,", "Ensalada,", "Pasta,", "Helado,", "Milanesa"})

platos_en_comun = Anita.intersection(Pepito)
siguen = len(platos_en_comun) * 100
siguen = siguen / 6
print("Siguen Saliendo?:", siguen > 50)


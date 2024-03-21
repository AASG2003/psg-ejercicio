# Dos mochileros se encuentran en el Salar de Uyuni y se ponen 
# a comparar la cantidad de lugares que han visitado
# Cada uno quiere saber en que parte del mundo ha estado el 
# otro que el no haya visitado
# mochilero_a = {"París", "Londres", "Nueva York", "Tokio",
# "Peru", "Chile", "Colombia", "Bolivia"}

# mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney",
# "Argentina","Brasil","Panama","Bolivia"}

mochilero_a = {"París", "Londres", "Nueva York", "Tokio",
"Peru", "Chile", "Colombia", "Bolivia"}
mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney",
"Argentina","Brasil","Panama","Bolivia"}
mochilero_a_lugares_faltantes = mochilero_b - mochilero_a
mochilero_b_lugares_faltantes = mochilero_a - mochilero_b
print("El mochilero a no ha visitado:", mochilero_a_lugares_faltantes)
print("El mochilero b no ha visitado:", mochilero_b_lugares_faltantes)

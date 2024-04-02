# cambiar = "Pizza, Tacos, Ensalada, Pasta, Helado, Milanesa"
# cambiar = cambiar.replace(" ", '", "')
# print(cambiar)
correo = input("Introduce un correo:")
arroba = correo.index("@") 
mail = correo[:arroba:1]
arroba += 1
domain = correo.index(".com")
domain = correo[arroba:domain:1]

if mail and domain and not domain.count("@") and domain.find("."):
    print("Correo valido")
else:
    print("Correo Invalido")

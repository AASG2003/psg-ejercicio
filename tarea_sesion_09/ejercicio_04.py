# Tienes una tienda de abarrotes y tienes dos listas una 
# con los productos que tienes y otra con los precios
# Agregar 5 productos nuevos al final de las listas
# Eliminar el producto con el nombre "Leche" de las listas
# Cuanto cuesta el producto "Pan" y "Huevo"
# Cual es el producto más caro y más barato

productos = ["Leche", "Cereal", "Yogurt"]
precios = [4, 15, 9]
productos.extend(["Huevo", "Pan", "Refresco", 
                  "Cafe", "Pastel"])
precios.extend([12, 8, 9, 15, 20])
leche = productos.index("Leche")
productos.pop(leche)
precios.pop(leche)
print(productos)
print(precios)
print("Precio pan:", precios[productos.index("Pan")])
print("Precio huevo:", precios[productos.index("Huevo")])
print("Producto mas caro:", productos[precios.index(max(precios))])
print("Producto mas caro:", productos[precios.index(min(precios))])

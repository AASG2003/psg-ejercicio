# Tienes una tienda de abarrotes y tienes dos listas una con 
# los productos que tienes y otra con los precios 5. Cuantos 
# productos tienes en total 6. Cuanto cuesta el total de los 
# productos 7. Ordena los productos alfabéticamente y precios 
# si es posible 8. Eliminar todos los productos de las listas
productos = ["Leche", "Cereal", "Yogurt"]
precios = [4, 15, 9]
productos.extend(["Huevo", "Pan", "Refresco", 
                  "Cafe", "Pastel"])
print("Cantidad de productos:",len(productos))
print("Costo total de productos:",sum(precios))
##Falta completar
productos.clear()
precios.clear()
print("Productos:", productos)
print("Precios:", precios)


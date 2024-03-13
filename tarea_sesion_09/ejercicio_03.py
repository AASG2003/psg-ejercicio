# Crear una lista de personas con 10 nombres de personas
# Obtener una sublista de 2 a 7
# Buscar si existe el nombre "Jhon" en la lista original
# Ordenar la sublista alfabéticamente
# Ordenar la lista original alfabéticamente de forma 
# descendente

personas = ["Danna", "Bernardo", "Sergio", "Jonathan", 
            "Tatiana", "Andres", "Adriana", "Andrei",
            "Fernando", "Juan"]
personas_subLista = personas[1:7:1];
print("Sublista 2 a 7:", personas_subLista)
print("Esta Jhon en la lista:", "Jhon" in personas)
personas_subLista.sort()
print("Sublista Ordenada:", personas_subLista)
personas.sort(reverse=True);
print("Lista original ordenada al reves:", personas)



def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    name = input("Escribe tu nombre")
    surname = input("Escribe tu apellido")
    nombre_completo = (name + " " + surname)
    print(nombre_completo.lower())
    print(nombre_completo.title())
    print(nombre_completo.upper())
    print("\t" + nombre_completo.lower())

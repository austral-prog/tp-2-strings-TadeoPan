def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input("Nombre:").lower()
    print("Contiene a:", "a" in nombre)
    print("Contiene b:", "b" in nombre)
    print("Contiene c:", "c" in nombre)
    print("Contiene d:", "d" in nombre)
    print("Contiene e:", "e" in nombre)

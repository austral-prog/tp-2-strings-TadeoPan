def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gastos = float(input("Ingresar gasto:"))
    print(gastos)
    dinero_recibido = int(input("Dinero recibido"))
    print(dinero_recibido)
    vuelto = dinero_recibido - gastos
    print( "\n" "Vuelto")
    pesos = int(vuelto)
    print( "\n" "Pesos:")
    print(pesos)
    centavos = int((vuelto - pesos)*100)
    print("Centavos:")
    print(centavos)

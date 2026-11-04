colores=["azul","morado","rojo","amarillo","negro"]
for contador in colores:
    print(contador)
    #Si el color actual es "Rojo", detener el bucle
    if contador=="Rojo":
        print("color encontrado! saliendo del bucle")
        encontrado=True
        break
    
#el mapa del tesoro
mapa=[
    [".",".",".","."],
    [".",".","B","."],
    [".",".",".","."],
    [".","A",".","."]
]
filas=len(mapa)
columnas=len(mapa[0])
#Recorriendo con ciclos anidados
#Ciclo externo para mejorar filas(i)
for i in range(filas):
    #Ciclo externo para mejorar columnas(j)
    for j in range(columnas):
        #verificamos si encontramos el tesoro
        if mapa[i][j]=="A":
            print(f"tesoro encontrado en la posicion[{i}][{j}]")
            if mapa[i][j]=="B":
                 print(f"tesoro encontrado en la posicion[{i}][{j}]")
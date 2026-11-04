#Matriz
Matriz=[
    ["a","b","c","d","e","f","g"],
    ["h","i","j","k","l","m","n"],
    ["ñ","o","p","q","r","s","t"],
    ["u","v","w","x","y","z"],
]
for i in range(0,7):
    #cico interno para el indice de las columnas(j)
    for j in range(0,4):
        print(f"posicion[{i}][{j}]={Matriz[i][j]}")

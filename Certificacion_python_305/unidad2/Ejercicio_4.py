promedio=[6,8,1,7,8,9]
# promedio bajo
promedio_bajo=promedio[0]
for contador in promedio:
    if contador<promedio_bajo:
        promedio_bajo=contador
print("el promedio mas bajo es:",promedio_bajo)
# promedio lto
promedio_alto=promedio[0]
for contador in promedio:
    if contador > promedio_alto:
        promedio_alto = contador
print("el promedio mas alto es:",promedio_alto)

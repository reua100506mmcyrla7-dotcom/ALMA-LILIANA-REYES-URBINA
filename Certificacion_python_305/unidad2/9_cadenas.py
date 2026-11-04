#cadenas y concatenacion con (+)
cadena1='Hola'
cadena2='Mundo'
multilinea="""Esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
#cadenas y repeticion 
eco="ja"*3
print(eco)
#cambiar una cadena de minuscula a mayuscula
tu_nombre='Alma Lilina'
print(tu_nombre.upper())
#cambiar de mayuscula a minuscula 
print(tu_nombre.lower())
#remplazar un texto en una cadena
frase="megusta programacion"
print(frase.replace("programacion","matematicas"))
#formato de concatenar cadenas (F-string)
edad=16
nombre='Alma Liliana'
mensaje=f"hola,me llamo{nombre} y tengo\n{edad}años"
print(mensaje)
#contar las caracteristicas de una cadena 
texto="¡Felicidades por continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto contiene una palabra 
oracion="aprender python es divertido"
if "python" in oracion:
    print("encontrado")
else:
    print("no esta")
    #validar contenido de una cadena 
    cadena="a1"
    print(cadena.isalpha())#true
    print(cadena.isdigit())#false
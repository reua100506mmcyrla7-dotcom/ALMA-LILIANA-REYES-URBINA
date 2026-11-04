#creando un diccionario en python
persona={
    "nombre":"sofia",
    "edad":28,
    "profesion":"ingeniera",
    "estudiante":False
}
print(persona)
#accediendo a un valor especifico
print(persona["profesion"])
#se puede usar el metodo .get()
#es util por que no da error si la clave n existe
print(persona.get("edad"))
#modificar un valor existente
persona["edad"]=29
print(persona.get("edad"))
#agregar un par (clave:valor)
persona["ciudad"]="san pepe"
print(persona)
#recorrer un diccionario con un bucle
for clave,valor in persona.intems():
    print(f"{clave}:{valor}")
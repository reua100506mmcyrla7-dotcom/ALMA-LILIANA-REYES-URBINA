#1 . creamos un diccionario
nuevo_usuario={}
#2 . pedimos los datos desde el teclado
nuevo_usuario["nombre"]= input("ingresa el nombre:")
nuevo_usuario["edad"]= int (input("ingresa la edad:"))
nuevo_usuario["estatura"]= float(input("ingresa tu estatura"))
print("\n ---informacion guardada---")
#mostrando la informacion del diccionario
print(nuevo_usuario)
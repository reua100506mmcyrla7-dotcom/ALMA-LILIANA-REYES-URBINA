carrito=[]#Lista vacia
n_productos=int(input("ingresa el numero de productos"))
for i in range(n_productos):
    producto=input("ingresa el producto a tu carrito")
    carrito.append(producto)
print("Lista creada correctamente")
carrito[0]="coca"
print(f"tu carrito contiene{carrito}")
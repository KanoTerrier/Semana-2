"""
Pida el nombre del cleinte, cuantas manzanas comprará y un precio. 
Muestre el nombre y el total a pagar
"""
print("Ingrese su nombre: ")
nomCli = input()

print(f"Hola {nomCli}")

print("¿Cuántas manzanas deseas comprar? ")
Comp = int(input())

print(f"Deseo comprar {Comp}")

manzana = 2
costo_final = manzana * Comp

print(f"Tienes que pagar {costo_final}")
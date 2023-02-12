print(not True)
print(not False)
print()
# or

#negar el resultado todo lo contrario(si es true lo pasa a false y viceversa)
print("True and True =", not (True and True))
print("True and False =", not (True and False))
print("False and True =", not (False and True))
print("False and False =", not (False and False))

print()
stock = input("numero de stock: ")
stock = int(stock)

print(not (100 <= stock <= 1000)) #ay hpta simplificacion

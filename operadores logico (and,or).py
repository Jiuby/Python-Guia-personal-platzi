#and
print("AND")

#tiene q ser verdaderos las dos partes de la operacion para que saque True(verdadero)
print("BOOLEANOS")
print("True and True =", True and True)
print("True and False =", True and False)
print("False and True =", False and True)
print("False and False =", False and False)
print()

#ahora con enteros
print("ENTEROS")
print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

#ahora con input(input siempre empieza siendo str)

stock = input("numero de stock: ")
stock = int(stock)  #solucion mas practica stock = int(input("numero de stock: "))
                    # lo que hacemos es volverlo entero

print(stock >= 100 and stock <= 1000)
print()

#or
print("OR")

#solo uno debe de ser True(Verdadero)
print("BOOLEANOS")
print("True or True =", True or True)
print("True or False =", True or False)
print("False or True =", False or True)
print("False or False =", False or False)
print()


role = input("cual es su rol: ")
print(role == "admin" or role =="seller")
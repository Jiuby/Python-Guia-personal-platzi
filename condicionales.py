# if siempre es de operacion boolean

if False:
    print("no debe de ejecutarse")

if True:
    print("debe de ejecutarse")
print()

#solo if
"""
#ejemplo con input string
pet = input("cual es tu mascota favorita: ")
#si no se cumple ninguna condicion no pasa nada

if pet == "perro":
    print("morite")

if pet == "gato":
    print("me caes bien")
"""

#if and else
"""stock = int(input("escriba su stock:"))

if 100 <= stock <= 1000:
    print("el stock es correcto")
else: #si no cumple la condicion cumpla la siguiente instruccion
    print("no es correcto")"""

pet = input("cual es tu mascota favorita: ")

#si no se cumple la instruccion que (evalue la otra condicion)elif
if pet == "perro":
    print("morite")
elif pet == "gato":
    print("me caes bien")
elif pet == "pez":
    print("que")
else:
    print("vos q putas tienes")
"""
{} = diccionario
[] = listas
() = tuplas
"""

diccionario = {}
print(type(diccionario))

diccionario = {  #normalmente vienen como strings
    "nombre": "Juan",
    "apellido": "velez",
    "avion": "bla bla bla",
    "age": 17
}

print(diccionario)
print(len(diccionario))  # el nombre,apellido,avion y edad el resto es la descripcion

print(diccionario["apellido"])  #  no se pregunta por el index si no por el nombre
print(diccionario["nombre"])
print(diccionario.get("age"))  # si no hay valor nos suelta algo
print(diccionario.get("pablo"))

print("avion" in diccionario)
print("panadero" in diccionario)
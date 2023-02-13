#esta vez es hacer crud en los diccionarios
persona = {
    "nombre": "Juan",
    "apellido": "Velez",
    "lenguajes": ["python", "Java"],
    "age": 17
}
print(persona)

#  actualizar las cosas
persona["nombre"] = "fuan"  #  no es con index, solo con el nombre
persona["age"] -= 2  #  le podemos agregar aritmetica
persona["lenguajes"].append("HTML")  #  en el tema de las listas modificarlo como una misma
print(persona)

#  eliminar
del persona["apellido"]
persona.pop("age")
print(persona)
print()

#  ver que tiene
print("items")  #  mostrarme que tiene y el valor
print(persona.items())

print("keys")  #  mostrarme que tiene y NO el valor
print(persona.keys())

print("values")  #  mostrarme los valores y No que tiene
print(persona.values())
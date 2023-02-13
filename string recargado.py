#in para buscar si java se encuentra en la cadena texto
#string recargado son metodos para poder jugar con el texto



texto = "Maricon orangutan"
"""
print("Java" in texto)
print("Maricon" in texto)  #ojo con las mayusculas

print()

#tambien podemos jugar con if
if "orangutan" in texto:
    print("uga uga")
else:
    print("no uga uga")
print()
"""
#metodo para evaluar el tamaño de un string

tamaño = len("texto   ")  #si hay espacios son considerados un caracter
print(tamaño)
print(len(texto))  #una forma mas acortada

print(texto, texto.upper())  #mayuscula
print(texto, texto.lower())  #minuscula

"""
si = texto.upper()
print(si)
"""

print(texto.count("a"))  #contar las veces que sale una letra
print(texto.swapcase())  #caracter en mayuscula a minuscula y viceversa

#metodo booleano
print(texto.startswith("m"))
print(texto.endswith("orangutan"))

#reemplaza texto o palabras
print(texto.replace("a", "e"))
print(texto.replace("Maricon", "Hetero"))

text = "esto  se supone q es un titulo"
print(text)
print(text.capitalize())  #primer caracter en mayuscula
print(text.title())  #el inicio de cada palabra en mayuscula

print(text.isdigit())
print("392".isdigit())  #solo funciona con strings y no con enteros




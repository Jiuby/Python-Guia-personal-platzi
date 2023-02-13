#esto es para saber el numero de la posicion del texto
#usar los corchetes para esto []

texto = "El diablo"
print(texto[2])
print(texto[0])
"print(texto[1000])"
tamaño = len(texto)
print(f"el tamaño es de {tamaño}")

#para buscar la ultima letra
print(texto[tamaño - 1])
print(texto[-1])

#slicing
print(texto[3:9])  #tener mucho cuidado seleccionando
print()

print(texto[:7])  #si no envias nada por defecto comienza en cero
print(texto[3:-1])
print(texto[3:])  #si no envias nada por defecto va hasta el final

print(texto[:])
print()

#saltos
print(texto[3:9:1])
print(texto[3:9:2])
print(texto[::2])
print(texto[::1])
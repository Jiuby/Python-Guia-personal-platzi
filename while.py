"""
while True:  #ciclo infinito
    print("se ejecuto")
    """
"""
contador = 0

#  tener cuidado con la sangria
while contador < 10:
    contador += 1
    print(contador)
    """
"""
contador = 0

while contador < 20:
    contador += 1
    if contador == 15:
        break
    print(contador)"""

counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        continue  #salta al siguiente ciclo osea todos los datos anteriores que recolecto se descartan
    print(counter)
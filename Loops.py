"""for element in range(1, 21):
    print(element)
"""

mi_lista = [1, 3, 4, 6, 71, 34, 15]
for i in mi_lista:
    print(i)

mi_tupla = ("juan", "velez" ,"esteban")
for i in mi_tupla:
    print(i)
print()

product = {
    "producto": "camisa",
    "precio":  100,
    "stock": 89
}

for i in product:
    print("valor: ", product[i])
print()

for i in product:
    print("llave: ", i)
print()

for key in product:
    print(key, "=", product[key])
print()

for key, value in product.items():
    print(key, "=", value)

personas = [
    {
        "name": "nico",
        "age": 34
    },
    {
        "name": "juan",
        "age": 17
    },
    {
        "name": "wilson",
        "age": 5
    }
]


for person in personas:
    print(person["name"])
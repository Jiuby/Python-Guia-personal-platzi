#tener cuidado con los flotantes para las comparaciones
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)
print()

#volvemos Y una string y le decimos q solo nos deje 2 digitos (forma string
y_string = format(y, ".2g")
print(y_string)
print(y_string == str(x))
print()


#forma matematica
print(y, x)

tolerance = 0.00001
print(abs(x - y) < tolerance) #abs es el valor absoluto del resultado de x - y
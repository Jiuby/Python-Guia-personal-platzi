usuario = input("piedra, papel o tijera: ")
computadora = "tijera"

if usuario == computadora:
    print("empate")
elif usuario == "piedra": # si el usuario digita esto se comienza a cumplir lo de abajo
    #estas son las condiciones del computador
    if computadora == "tijera":
        print("piedra gana a tijera")
        print("gano el usuario")
    else:
        print("papel gana a piedra")
        print("gano la computadora")
elif usuario == "papel":
    if computadora == "piedra":
        print("papel gana a piedra")
        print("gano el usuario")
    else:
        print("tijera gana a papel")
        print("gano el computador")
elif usuario == "tijera":
    if computadora == "papel":
        print("tijera gana a papel")
        print("gano el usuario")
    else:
        print("piedra gana a tijera")
        print("gano el computador")
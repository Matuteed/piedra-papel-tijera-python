

ronda = 1

while True: 
    print(f"Número de ronda {ronda}")

    nombre1 = input("¡Hola, jugador 1! ¿Cuál es tu nomrbre?: ")
    nombre2 = input("¡Hola, jugador 2! ¿Cuál es tu nombre?: ")

    jugador1 = input(f"{nombre1}, ¿Qué eliges: piedra, papel o tijera?: ").lower()
    jugador2 = input(f"{nombre2}, ¿Qué eliges: piedra, papel o tijera?: ").lower()

    condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

    if jugador1 == jugador2:
        print("¡Ha sido un empate!")
    elif (condicion1) or (condicion2) or (condicion3):
        print(f"¡Felicidades,{nombre1}! Has ganado.")
    else:
        print(f"¡Felicidades, {nombre2} Has ganado.")
    otra_ronda = input("¿Quieren jugar otra ronda? (sí/no): ").strip().lower()
    if otra_ronda not in ["sí", "si"]:
        print("¡Gracias por jugar! ¡Hasta la próxima!")
        break

    ronda += 1
    

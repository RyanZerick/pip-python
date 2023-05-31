import random

OPCIONES = {"piedra": 1,
                "papel": 2,
                "tijera": 3}
SALIR = ["exit", "salir"]

def validar_opcion(cadena):
    list_opciones = list(OPCIONES.keys())
    valor = str(cadena).lower()

    if valor in list_opciones or valor in SALIR:
        return valor
    else:
        return False

def yankenpo(eleccion, win_pc, win_user, draw):

    eleccion_pc = random.randint(1,3)
    eleccion_user = OPCIONES[eleccion]

    if eleccion_pc == eleccion_user:
        draw += 1
        print("empate")
    elif (eleccion_pc == 1 and eleccion_user == 3) or (eleccion_pc == 2 and eleccion_user == 1) or (eleccion_pc == 3 and eleccion_user == 2):
        win_pc += 1
        print("gano la PC")
    else:
        win_user += 1
        print("gano el usuario")

    return win_pc, win_user, draw

def main():

    introduccion = ["Bienvenido al Juego de Piedra Papel o tijeras", 
                    "El juego solo tiene por regla que escojas un valor dentro de los 3 indicados", 
                    "En caso escribas otra cosa, el juego simplemente volvera a solicitar un valor correcto", 
                    "en caso de querer salir, escribir EXIT"]
    
    mensaje = ["Round: ", "Usuario: ", "IA: "]
    error_message = "recuerda que los valores posibles son: piedra, papel, tijera o salir, exit"
    contador = 0
    win_pc = 0
    win_user = 0
    draw = 0

    for x in introduccion:
        print(x)
    
    while(True):
        if contador == 0:
            print(mensaje[0] + str(contador))
        else:
            print(mensaje[0] + str(contador))
            print(mensaje[1] + str(win_user))
            print(mensaje[2] + str(win_pc))
        while(True):
            valor = validar_opcion(input("escriba una opcion:"))
            if valor != False:
                break
            else:
                print(error_message)
        if valor in SALIR:
            print("Gracias por jugar")
            break

        win_pc, win_user, draw = yankenpo(valor,win_pc,win_user,draw)

        contador += 1
      

if __name__ == "__main__":
    main()
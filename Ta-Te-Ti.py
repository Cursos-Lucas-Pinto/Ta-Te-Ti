tablero = [["|_|","|_|","|_|"],["|_|","|_|","|_|"],["|_|","|_|","|_|"]]

simbolo_1 = None
simbolo_2 = None
cont_pos = 0
hay_un_ganador = False

def ganar_si():
        #Comprobar si el Jugador 1 ganó el juego
        if (simbolo_1 in tablero[0][0]) and (simbolo_1 in tablero[0][1]) and (simbolo_1 in tablero[0][2]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_1 in tablero[1][0]) and (simbolo_1 in tablero[1][1]) and (simbolo_1 in tablero[1][2]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_1 in tablero[2][0]) and (simbolo_1 in tablero[2][1]) and (simbolo_1 in tablero[2][2]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_1 in tablero[0][0]) and (simbolo_1 in tablero[1][0]) and (simbolo_1 in tablero[2][0]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_1 in tablero[0][1]) and (simbolo_1 in tablero[1][1]) and (simbolo_1 in tablero[2][1]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_1 in tablero[0][2]) and (simbolo_1 in tablero[1][2]) and (simbolo_1 in tablero[2][2]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_1 in tablero[0][0]) and (simbolo_1 in tablero[1][1]) and (simbolo_1 in tablero[2][2]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_1 in tablero[0][2]) and (simbolo_1 in tablero[1][1]) and (simbolo_1 in tablero[2][0]):
            hay_un_ganador = True
            return hay_un_ganador
        
        #Comprobar si el Jugador 2 ganó el juego
        elif (simbolo_2 in tablero[0][0]) and (simbolo_2 in tablero[0][1]) and (simbolo_2 in tablero[0][2]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_2 in tablero[1][0]) and (simbolo_2 in tablero[1][1]) and (simbolo_2 in tablero[1][2]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_2 in tablero[2][0]) and (simbolo_2 in tablero[2][1]) and (simbolo_2 in tablero[2][2]):
            hay_un_ganador = True
            return hay_un_ganador
        
        elif (simbolo_2 in tablero[0][0]) and (simbolo_2 in tablero[1][0]) and (simbolo_2 in tablero[2][0]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_2 in tablero[0][1]) and (simbolo_2 in tablero[1][1]) and (simbolo_2 in tablero[2][1]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_2 in tablero[0][2]) and (simbolo_2 in tablero[1][2]) and (simbolo_2 in tablero[2][2]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_2 in tablero[0][0]) and (simbolo_2 in tablero[1][1]) and (simbolo_2 in tablero[2][2]):
            hay_un_ganador = True
            return hay_un_ganador

        elif (simbolo_2 in tablero[0][2]) and (simbolo_2 in tablero[1][1]) and (simbolo_2 in tablero[2][0]):
            hay_un_ganador = True
            return hay_un_ganador

def mostrar_tablero():
    for fila in range(0,3):
        for columna in range(0,3):
            print(tablero[fila][columna], end = "")
    
        print("")

def insertar_simbolo(simbolo):
    ocupada = 0
    fila = ""
    columna = ""
    
    while ("1" not in fila) and ("2" not in fila) and ("3" not in fila):
        print("Ingrese la fila en la que quiere insertar el simbolo (1 , 2 o 3):")
        fila = input()

    while ("1" not in columna) and ("2" not in columna) and ("3" not in columna):
        print("Ingrese la columna en la que quiere insertar el simbolo (1 , 2 o 3):")
        columna = input()
    
    fila = int(fila)
    columna = int(columna)

    if tablero[fila-1][columna-1] != "|_|":
        print("\nPosición ocupada.")
        ocupada = 1

        mostrar_tablero()
    else:
        tablero[fila-1][columna-1] = "|" + simbolo + "|"

        mostrar_tablero()
    
    return ocupada


#Muestro la tabla vacia
mostrar_tablero()

#Valido el valor ingresado por el Jugador 1
print("Jugador 1")
while True:
    if(simbolo_1 == "X" or simbolo_1 == "O"):
        break
    else:
        print("Elige un simbolo: (X / O):")
        simbolo_1 = input()

print("El simbolo del Jugador 1 es:\n", simbolo_1)

#Asigno un simbolo al Jugador 2 segun el simbolo elegido por el Jugador 1
if(simbolo_1 == "X"):
    simbolo_2 = "O"
else:
    simbolo_2 = "X"

print("El simbolo del Jugador 2 es:\n", simbolo_2)

while True:
    #El jugador que tiene la 'X', comienza la partida
    if simbolo_1 == "X":
        
        print("Jugador 1:")

        ocupada = 1
        
        while ocupada == 1:
            ocupada = insertar_simbolo(simbolo_1)

        cont_pos += 1

        hay_un_ganador = ganar_si()
        if hay_un_ganador == True:
            print("El ganador es: Jugador 1.")
            break

        if cont_pos == 9:
            print("Empate.")
            break
        
        print("Jugador 2:")

        ocupada = 1

        while ocupada == 1:
            ocupada = insertar_simbolo(simbolo_2)

            fila = 0
            columna = 0
        
        cont_pos += 1

        hay_un_ganador = ganar_si()
        if hay_un_ganador == True:
            print("El ganador es: Jugador 2.")
            break

        if cont_pos == 9:
            print("Empate.")
            break

    else:
        print("Jugador 2:")
        
        ocupada = 1
        
        while ocupada == 1:
            ocupada = insertar_simbolo(simbolo_2)

            fila = 0
            columna = 0

        cont_pos += 1

        hay_un_ganador = ganar_si()
        if hay_un_ganador == True:
            print("El ganador es: Jugador 2.")
            break

        if cont_pos == 9:
            print("Empate.")
            break

        print("Jugador 1:")
        
        ocupada = 1

        while ocupada == 1:
            ocupada = insertar_simbolo(simbolo_1)

            fila = 0
            columna = 0

        cont_pos += 1

        hay_un_ganador = ganar_si()
        if hay_un_ganador == True:
            print("El ganador es: Jugador 1.")
            break

        if cont_pos == 9:
            print("Empate.")
            break
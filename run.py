#!/usr/bin/python
# -*- coding: latin-1 -*-

import games
import heuristics

game = games.ConnectFour()
state = game.initial

count = 1
initialPlayer = raw_input("¿Quiere comenzar la partida? (pulse 'yes' / 'no') : ")

while (initialPlayer != 'yes') and (initialPlayer != 'no') and (count <= 3):
    initialPlayer = raw_input("Opción incorrecta. Vuelva a introducir el valor : ")
    count += count

if(initialPlayer == 'yes'):
    player = 'human'
elif(initialPlayer == 'no'):
    player = 'machine'
else:
    print("Ha superado el número máximo de intentos. Empezará la máquina.")
    player = 'machine'

count = 1
dificultad = raw_input("Elija nivel de dificultad: \n 1-Fácil\n 2-Medio \n 3-Difícil \n")
dificultad = int(dificultad)


while (dificultad < 1) and (dificultad > 3) and (count <= 3) :
    dificultad = raw_input("Opción incorrecta. Vuelva a introducir el nivel : ")
    dificultad = int(dificultad)
    count += count

heuristica = heuristics.h
if(dificultad == 1):
    d = 1
elif(dificultad == 2):
    d = 2
elif(dificultad == 3):
    d = 4
else:
    print("Ha superado el número máximo de intentos. Su nivel de dificultad será medio.")
    d = 2

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'human':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        player = 'machine'
    else:
        print "Thinking..."
        #move = games.alphabeta_full_search(state, game)
        move = games.alphabeta_search(state, game,d, eval_fn=heuristica)
        state = game.make_move(move, state)
        player = 'human'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break


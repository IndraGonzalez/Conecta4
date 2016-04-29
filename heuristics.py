import random

def h0(state):
    board = state.board.copy()
    x=1
    y=1
    v=6
    h=7
    while (y<=v) and (x<=h):
        celda = board.get((x, y))
        # Hay que pasar cuál es el jugador e ir mirando las celdas a su alrededor
        #FACIL = horizontal y vertical
        #MEDIO = diagonales también
        #DIFICIL = lo anterior y que intente ganar
        if(celda=='X'):
            h +=1
        y += y
        x += x
    h = random.random()
    print h
    return h

def h1(self):
    return random.random()

def h2(self):
    return random.random()

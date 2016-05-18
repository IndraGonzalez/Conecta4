import random


def h(state):
    return get_heuristic(state)

def get_adversary(player):
    if (player == 'O'):
        return 'X'
    else:
        return 'O'

def get_heuristic(state):

    board = state.board.copy()
    player = state.to_move
    adversary = get_adversary(player)
    heuristic = 0

    if(state.utility != 0):
        return state.utility*1000000000

    moves = legal_moves(state)
    i = 1
    while(i <= len(moves)-1):
        move = moves[i]
        heuristic += find_connect(board,move,player,(0,1))
        heuristic += find_connect(board,move,player,(1,0))
        heuristic += find_connect(board,move,player,(1,-1))
        heuristic += find_connect(board,move,player,(1,1))

        heuristic -= find_connect(board,move,adversary,(0,1))
        heuristic -= find_connect(board,move,adversary,(1,0))
        heuristic -= find_connect(board,move,adversary,(1,-1))
        heuristic -= find_connect(board,move,adversary,(1,1))

        i += 1

        """display(board,6,7)
        print("\nHeuristica: ")
        print(heuristic)"""


    return heuristic


def find_connect(board, move, player, (delta_x, delta_y)):
    # h -> heuristica parcial que se sumara o restara a la total
    h = 0
    # i -> numero de posiciones recorridas
    i = 0
    adversary = get_adversary(player)
    x,y = move

    while board.get((x, y)) != adversary:
        if x > 7 or x < 0 or y > 6 or y < 0:
             break
        if(board.get((x, y)) == player):
            h += 5
        else: h += 1
        i += 1
        x, y = x + delta_x, y + delta_y

    x, y = move
    while board.get((x, y)) != adversary:
        if x > 7 or x < 0 or y > 6 or y < 0:
             break
        if(board.get((x, y)) == player):
            h += 5
        else: h += 1
        i += 1
        x, y = x - delta_x, y - delta_y

    i -= 1

    if i >= 4:
        return h
    else:
        return 0

def legal_moves(state):
    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y-1) in state.board]

def display(board, v, h):
    for y in range(v, 0, -1):
        for x in range(1, h + 1):
            print board.get((x, y), '.'),
        print
    print "-------------------"
    for n in range(1, h + 1):
        print n,

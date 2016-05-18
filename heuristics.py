import utils

def memoize(f):
    memo = {}
    def dictionary(state):
        key = tuple(state.board.items())
        if key not in memo:
            memo[key] = f(state)
        return memo[key]
    return dictionary

@memoize

def h(state):

    board = state.board
    player = state.to_move
    adversary = 'O'
    heuristic = 0

    if(state.utility != 0):
        return state.utility*utils.infinity


    for move in legal_moves(state):
        heuristic += find_connect(board,move,player,(0,1))
        heuristic += find_connect(board,move,player,(1,0))
        heuristic += find_connect(board,move,player,(1,-1))
        heuristic += find_connect(board,move,player,(1,1))

        heuristic -= find_connect(board,move,adversary,(0,1))
        heuristic -= find_connect(board,move,adversary,(1,0))
        heuristic -= find_connect(board,move,adversary,(1,-1))
        heuristic -= find_connect(board,move,adversary,(1,1))

    return heuristic

def find_connect(board, move, player, (delta_x, delta_y)):
    # h -> heuristica parcial que se sumara o restara a la total
    h = 0
    # i -> numero de posiciones recorridas
    i = 0
    adversary = 'O'
    x,y = move

    while board.get((x, y)) != adversary:
        if x > 7 or x < 0 or y > 6 or y < 0:
             break
        if(board.get((x, y)) == player):
            h += 5
        else:
            h += 1
        i += 1
        x, y = x + delta_x, y + delta_y

    x, y = move
    while board.get((x, y)) != adversary:
        if x > 7 or x < 0 or y > 6 or y < 0:
             break
        if(board.get((x, y)) == player):
            h += 5
        else:
            h += 1
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
import utils

def memoize(f):
    memo = {}
    def dictionary(state,player):
        key = tuple(state.board.items())
        if key not in memo:
            memo[key] = f(state,player)
        return memo[key]
    return dictionary


def getAdversary(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'


@memoize
def h(state,player):

    board = state.board
    adversary = getAdversary(player)
    heuristic = 0

    if(state.utility != 0):
        if(player == 'X'):
            return state.utility*utils.infinity
        else:
            return -1 * state.utility*utils.infinity


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
    adversary = getAdversary(player)

    x,y = move

    while board.get((x, y)) != adversary:
        if x > 7 or x < 0 or y > 6 or y < 0:
             break
        if(board.get((x, y)) == player):
            h += 6
        else:
            h += 2
        i += 1
        x, y = x + delta_x, y + delta_y

    x, y = move
    while board.get((x, y)) != adversary:
        if x > 7 or x < 0 or y > 6 or y < 0:
             break
        if(board.get((x, y)) == player):
            h += 6
        else:
            h += 2
        i += 1
        x, y = x - delta_x, y - delta_y

    i -= 1
    #h -= 12
    h -= 4

    if i >= 4:
        return h
    return 0


def legal_moves(state):
    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y-1) in state.board]
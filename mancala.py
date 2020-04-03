

#### NOTE: this has not been encorporated with Frank's game.py yet- this is just a basic structure

# valid_moves() returns the indexes of the pits that the player can choose from
# (i.e. the pits on their side that are not empty).
def valid_moves(board, player):
    moves = []
    for i in range(1,7):
        if board[player][i] != 0:
            moves.append(i)
    return moves


def main():
    board = [[0, 4, 4, 4, 4, 4, 4, 0],  # where [0][0] is the store of player 0, [1][7] is store of player 1
             [0, 4, 4, 4, 4, 4, 4, 0]]  # and [0][7], [1][0] are just placeholders

    possible_moves = [1, 2, 3, 4, 5, 6] #this is the index of available moves with respect to a given player
    player = 0

    while len(possible_moves) != 0:
        if player == 0: # human player's turn
            possible_moves = valid_moves(board, player) #check at beginning of turn

            # Do some stuff (get user input, move, ect.)

            if last_stone == 0: #if the last stone ended up in the store, take another turn (for computer this would be 7 not 0)
                player += 1

            possible_moves = valid_moves(board, player) #update

        else: #computer's turn
            pass

        player += 1
        player = player % 2


    winner = determine_winner(board)

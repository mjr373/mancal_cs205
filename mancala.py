

# valid_moves() returns the indexes of the pits that the player can choose from
# (i.e. the pits on their side that are not empty).
def valid_moves(board, player):
    # I'll fill this in soon
    pass


def main():
    board = [[4, 4, 4, 4, 4, 4, 0],  # FRANK replace this with whatever board you end up initializing
             [4, 4, 4, 4, 4, 4, 0]]

    possible_moves = [0, 1, 2, 3, 4, 5] #assumes all moves possible at beginning
    player = 0

    while len(possible_moves) != 0:
        if player == 0: # human player's turn
            possible_moves = valid_moves(board, player) #check at beginning of turn

            # Do some stuff (get user input, move, ect.)

            if last_stone[1] == 6: #if the last stone ended up in the store, take another turn
                player += 1

            possible_moves = valid_moves(board, player) #update

        else: #computer's turn
            pass

        player += 1
        player = player % 2


    winner = determine_winner(board)

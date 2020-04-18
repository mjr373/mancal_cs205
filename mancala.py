
# Import and initialize the pygame library
import numpy as np
import pygame
import pygame.freetype
import math
import random
import time

pygame.init()

#Constants
COLUMNS = 6
ROWS = 2
POCKET = 75
STORE = 100


width = POCKET * (COLUMNS + 1)
height = STORE * (ROWS + 1)

#Color Constants
WOOD = (193,154,107)
BLACK = (0,0,0)
BLUE = (0,0,255)

print(pygame.font.get_fonts())

#Set up images
start_image = pygame.image.load(r'game.jpg')
instruction_image = pygame.image.load(r'instructions.jpg')


#radius for pocket circles
pocket_radius = int(POCKET/2-5)

#Size of screen
size = [width + 200, height]

#Preparing font
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont("Britannic Bold", 30)

bigfont = pygame.font.SysFont("Britannic Bold", 35)

newfont = pygame.font.SysFont("arialnarrowboldttf", 20)

def instructions_screen():
    screen.fill(BLACK)
    screen.blit(instruction_image, (0,0))

    instructions_end = False
    while(instructions_end == False):

        instructions_label = newfont.render("-The top row and left store represents your side.", 1, (255, 0, 0))
        instructions_label2 = newfont.render("-When it is your turn, click on a pocket in the top row to move your pieces.", 1, (255, 0, 0))

        instructions_label6 = newfont.render("-If your last piece lands in your store, you take another turn", 1, (255, 0, 0))
        instructions_label7 = newfont.render("-If your last piece lands on an empty pocket on your side", 1, (255, 0, 0))
        instructions_label7_2 = newfont.render(" that piece and all adjacent pieces go to your store.", 1, (255, 0, 0))

        instructions_label3 = newfont.render("-The computer will make its move immediately after your turn.", 1, (255, 0, 0))
        instructions_label4 = newfont.render("-The game ends when no more moves can be made.", 1, (255, 0, 0))
        instructions_label5 = newfont.render("-The player with more pieces on their side at the end wins!", 1, (255, 0, 0))



        back = myfont.render(" - B A C K - ", 1, (255, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                if (posx >= 275 and posx <= 365 and posy >= 275 and posy <= 296):
                    instructions_end = True

        screen.blit(instructions_label, (0, 85))
        screen.blit(instructions_label2, (0, 110))
        screen.blit(instructions_label6, (0,135))
        screen.blit(instructions_label7, (0, 160))
        screen.blit(instructions_label7_2, (0, 175))
        screen.blit(instructions_label3, (0, 200))
        screen.blit(instructions_label4, (0, 225))
        screen.blit(instructions_label5, (0, 250))
        screen.blit(back, ((width)/2, 280))
        pygame.display.flip()


def start_screen():
    black = (0, 0, 0)
    game_start = False
    while (game_start == False):
        screen.fill(black)
        myfont = pygame.font.SysFont("Britannic Bold", 40)
        game_label = myfont.render("- Start Game", 1, (255, 0, 0))
        instructions_label = myfont.render("- Instructions", 1, (255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]

                print(posx, "posx")
                print(posy, "posy")
                if(posx >= 200 and posx <=370 and posy >= 150 and posy <= 173):
                    game_start = True
                elif(posx >= 200 and posx <=390 and posy >= 200 and posy <= 223):
                    instructions_screen()

        screen.blit(start_image,(0,0))
        screen.blit(game_label, (200, 150))
        screen.blit(instructions_label, (200, 200))
        pygame.display.flip()



def create_board():
    board = np.array([[0,4,4,4,4,4,4,0],[0,4,4,4,4,4,4,0]])
    return board

def update_board(new_board):
    board = new_board
    return board

def draw_board(board):
    screen.fill(BLACK)
    #Draw wooden board
    pygame.draw.rect(screen, WOOD, (50, 40, width+100, int(height/1.5)))
    #Draw the stores
    pygame.draw.ellipse(screen, BLACK, (65, 67, 65, 140))
    pygame.draw.ellipse(screen, BLACK, (585, 67, 65, 140))

    #Draw the store scores
    textsurface = bigfont.render(str(board[0][0]), False, BLUE)
    screen.blit(textsurface, (int(93), int(130)))

    textsurface = bigfont.render(str(board[1][7]), False, BLUE)
    screen.blit(textsurface, (int((6 * POCKET) + 163), int(130)))

    for c in range(COLUMNS):
        for r in range(ROWS):
            #Draw the pockets
            pygame.draw.circle(screen,BLACK, (int((c*POCKET)+170),int(r * POCKET+POCKET+25)), pocket_radius)
            if(not(r == 1 and c+1 == 6)):
                textsurface = myfont.render(str(board[r][c+1]), False, BLUE)
                screen.blit(textsurface, (int((c * POCKET)+170), int(r * POCKET+POCKET+25)))

    # Draw last pocket store
    textsurface = myfont.render(str(board[1][6]), False, BLUE)
    screen.blit(textsurface, (int((5 * POCKET) + 170), int(1 * POCKET + POCKET + 25)))

# valid_moves() returns the indexes of the pits that the player can choose from
# (i.e. the pits on their side that are not empty).
def valid_moves(board, player):
    moves = []
    for i in range(1,7):
        if board[player][i] != 0:
            moves.append(i)
    return moves


def move_pieces(pocket, board, player):
    num_pieces = board[player][pocket]
    board[player][pocket] = 0
    next_pocket = pocket
    for i in range(1, num_pieces+1):
        # user moves pieces
        if player == 0:
            next_pocket -= 1
            # pieces dropped on user's side of the board
            if (next_pocket >= 0) or (next_pocket <= -7):
                next_pocket = abs(next_pocket)
                if next_pocket == 7:
                    next_pocket = 6
                board[player][next_pocket] += 1
            # pieces dropped on computer's side of the board
            else:
                board[1][abs(next_pocket)] += 1

        # computer moves pieces
        if player == 1:
            next_pocket += 1
            # pieces dropped on computer's side of the board
            if (next_pocket <= 7) or (next_pocket >= 14):
                if next_pocket == 14:
                    next_pocket = 1
                board[player][next_pocket] += 1
            # pieces dropped on user's side of the board
            else:
                board[0][14-next_pocket] += 1
        
    # return index of last pocket a piece was dropped in
    # pair: (player side, pocket)
    if player == 0:
        if next_pocket < 0:
            player_side = 1
        else:
            player_side = 0
    if player == 1:
        if next_pocket > 7:
            player_side = 0
            next_pocket = 14-next_pocket
        else:
            player_side = 1

    return(player_side, abs(next_pocket))



# Determine if move player chose is possible
def is_valid_choice(pocket, board, player):
    available_moves = valid_moves(board, player)
    if pocket in available_moves:
        return True
    else:
        return False

def getXY(posx, posy):
    #GET COLUMN SELECTION
    if(posx >= 134 and posx <= 205):
        col = 1
    elif posx >= 210 and posx <= 280:
        col = 2
    elif posx >= 289 and posx <= 350:
        col = 3
    elif posx >= 360 and posx <= 430:
        col = 4
    elif posx >= 435 and posx <= 501:
        col = 5
    elif posx >= 510 and posx <= 580:
        col = 6
    else:
        col = 10000

    #GET ROW SELECTION
    if(posy >= 70 and posy <= 130):
        row = 0
    elif(posy >= 140 and posy <= 210):
        row = 1
    else:
        row = 100000
        
    return col, row

#moves all stones to the appropriate stores
def tabulate_score(board):
    store_0 = sum(board[0])
    store_1 = sum(board[1])
    board = np.array([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
    board[0][0] = store_0
    board[1][7] = store_1
    return board

screen = pygame.display.set_mode(size)

board = create_board()
player = 0  #where player 0 is user, player 1 is computer
possible_moves = valid_moves(board, player) #this is the index of available moves with respect to a given player

#Start screen is called before board is drawn
start_screen()
draw_board(board)



while len(possible_moves) != 0:
    board = update_board(board)
    draw_board(board)
    pygame.display.update()
    if player == 0: # human player's turn
        possible_moves = valid_moves(board, player) #check at beginning of turn

        #get user input
        valid_move = False
        while valid_move == False:
            event = pygame.event.wait()  #wait for user event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                posx = event.pos[0]
                posy = event.pos[1]

                col, row = getXY(posx, posy)

                if row == player:
                    #if col in possible_moves:
                    if is_valid_choice(col, board, player):
                        valid_move = True

        # Do some stuff (move, ect.)

        # return index of last pocket a piece was dropped in
        # pair: (player side, pocket)
        last_pocket_index = move_pieces(col, board, player)
        print(board)
        print("\n", last_pocket_index, "\n")

        board = update_board(board)
        draw_board(board)
        pygame.display.update()

        # if stone lands in empty pocket on user side
        if (last_pocket_index[0] == 0) and (last_pocket_index[1] not in possible_moves):
            if board[0][last_pocket_index[1]] == 1:
                board[0][0] += board[1][last_pocket_index[1]]
                board[0][0] += board[0][last_pocket_index[1]]
                board[1][last_pocket_index[1]] = 0
                board[0][last_pocket_index[1]] = 0

        possible_moves = valid_moves(board, player) #update

        if last_pocket_index[0] == 0 and last_pocket_index[1] == 0:
            print("player 0 goes again \n")
            player += 1
        else:
            print("player 0 turn over \n")


    else: #computer's turn
        possible_moves = valid_moves(board, player)
        move_index = random.randint(0, len(possible_moves) - 1)
        col = possible_moves[move_index]

        last_pocket_index = move_pieces(col, board, player)
        print("player 1 move: ", col)
        print(board)

        board = update_board(board)
        draw_board(board)
        pygame.display.update()

        # if stone lands in empty pocket on computer side
        if (last_pocket_index[0] == 1) and (last_pocket_index[1] not in possible_moves):
            if board[1][last_pocket_index[1]] == 1:
                board[1][7] += board[1][last_pocket_index[1]]
                board[1][7] += board[0][last_pocket_index[1]]
                board[1][last_pocket_index[1]] = 0
                board[0][last_pocket_index[1]] = 0

        possible_moves = valid_moves(board, player)

        if last_pocket_index[0] == 1 and last_pocket_index[1] == 7:
            print("player 1 goes again \n")
            player += 1
        else:
            print("player 1 turn over \n")


    player += 1
    player = player % 2
    
    board = update_board(board)
    draw_board(board)
    pygame.display.update()



def game_over(board):
    if board[0][1] == board[0][2] == board[0][3] == board[0][4] == board[0][5] == board[0][6] or board[1][1] == board[1][2] == board[1][3] == board[1][4] == board[1][5] == board[1][6]:
        return True

def determine_winner(board):
    if board[0][0] > board[1][7]:
        return "You win!"
    elif board[0][0] == board[1][7]:
        return "Tie Game :/"
    else:
        return "The computer wins :("



board = tabulate_score(board)
draw_board(board)
pygame.display.update()
print(board)



def end_screen():
    winner = determine_winner(board)
    your_score = board[0][0]
    comp_score = board[1][7]

    your_sentence = f"You scored {your_score} points!"

    computer_sentence = f"The computer scored {comp_score}  points!"
    black = (0, 0, 0)
    game_start = False
    while (game_start == False):
        screen.fill(black)
        #myfont = pygame.font.SysFont("Britannic Bold", 40)
        user_info = myfont.render((your_sentence), 1, (255, 0, 0))
        computer_info = myfont.render((computer_sentence), 1, (255, 0, 0))
        winner = myfont.render(determine_winner(board), 1, (255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        screen.blit(start_image, (0, 0))
        screen.blit(user_info, (175, 125))
        screen.blit(computer_info, (175, 155))
        screen.blit(winner, (175, 200))
        pygame.display.flip()

end_screen()



# Import and initialize the pygame library
import numpy as np
import pygame
import pygame.freetype

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

#radius for pocket circles
pocket_radius = int(POCKET/2-5)

#Size of screen
size = [width + STORE*2, height]

#Preparing font
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

bigfont = pygame.font.SysFont('Comic Sans MS', 35)


def create_board():
    board = np.array([[0,4,4,4,4,4,4,0],[0,4,4,4,4,4,4,0]])
    return board

def draw_board(board):



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
            if(not(r == 1 and c+1 ==6)):
                textsurface = myfont.render(str(board[r][c+1]), False, BLUE)
                screen.blit(textsurface, (int((c * POCKET)+170), int(r * POCKET+POCKET+25)))

    # Draw last pocket store
    textsurface = myfont.render(str(board[1][5]), False, BLUE)
    screen.blit(textsurface, (int((5 * POCKET) + 170), int(1 * POCKET + POCKET + 25)))





def move_pieces():
    pass

def is_valid_choice():
    pass



game_over = False
turn = 0





screen = pygame.display.set_mode(size)



board = create_board()

draw_board(board)

print(board)
while not game_over:
    #Main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if turn == 0:
                posx = event.pos[0]
                posy = event.pos[1]

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
                    col = 0

                #GET ROW SELECTION
                if(posy >= 70 and posy <= 130):
                    row = 1
                elif(posy >= 140 and posy <= 210):
                    row = 2



    pygame.display.update()


pygame.quit()




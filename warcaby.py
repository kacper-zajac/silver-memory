import pygame
import sys
import statistics


class Field:
    occupied = 0  # 0 - field free        1 - regular pionek    2 - damka
    team = "black"


Board = [[Field() for x in range(8)] for y in range(8)]

Board[0][0].occupied = 1            #ustawianie pionków
Board[2][0].occupied = 1
Board[4][0].occupied = 1
Board[6][0].occupied = 1

Board[1][1].occupied = 1
Board[3][1].occupied = 1
Board[5][1].occupied = 1
Board[7][1].occupied = 1

Board[0][2].occupied = 1
Board[2][2].occupied = 1
Board[4][2].occupied = 1
Board[6][2].occupied = 1

Board[1][7].occupied = 1
Board[1][7].team = "red"
Board[3][7].occupied = 1
Board[3][7].team = "red"
Board[5][7].occupied = 1
Board[5][7].team = "red"
Board[7][7].occupied = 1
Board[7][7].team = "red"

Board[0][6].occupied = 1
Board[0][6].team = "red"
Board[2][6].occupied = 1
Board[2][6].team = "red"
Board[4][6].occupied = 1
Board[4][6].team = "red"
Board[6][6].occupied = 1
Board[6][6].team = "red"

Board[1][5].occupied = 1
Board[1][5].team = "red"
Board[3][5].occupied = 1
Board[3][5].team = "red"
Board[5][5].occupied = 1
Board[5][5].team = "red"
Board[7][5].occupied = 1
Board[7][5].team = "red"



def move(w, l, W, L):
    Board[w][l].occupied = 0
    Board[W][L].occupied = 1
    Board[W][L].team = Board[w][l].team
    if Board[W][L].team is "black" and L is 7:
        Board[W][L].occupied = 2
        print("damka")
    if Board[W][L].team is "red" and L is 0:
        Board[W][L].occupied = 2


#zeby lepiej wygladalo ale nie pyka coś
'''                                 
def handle_space(x, y, w, l):
    if Board[x][y].occupied is 1 or Board[x][y].occupied is 2:
        if w < 0:
            return [x, y]
    else:
        if w > -1 and abs(w - x) == 1 and abs(l - y) == 1:
            move(w, l, x, y)
            return [-1, -1]
        elif w > -1 and abs(w - x) == 2 and abs(l - y) == 2 and Board[int((l + x) / 2)][int((l + y) / 2)].team is not Board[w][l].team:  # bicie
            Board[int((w + x) / 2)][int((l + y) / 2)].occupied = False
            #print(statistics.mean([w, x]))  # !!
            move(w, l, x, y)
            return [-1, -1]
        else:
            return [-1, -1]
    return [-1, -1]
'''

'''
def move_left(w, l):
    Board[w][l].occupied = False
    Board[w-1][l+1].occupied = True
'''

pygame.init()

gameDisplay = pygame.display.set_mode((704, 704))       # 704 podzielne przez 8
pygame.display.set_caption('Warcaby')
clock = pygame.time.Clock()               #nw po co

img = pygame.image.load("board2.png")
pionek = pygame.image.load("pionek.png")

gameDisplay.blit(img, (0, 0))
running = True

#filled_rect = pygame.Rect(44, 660, 15, 15)
#pygame.draw.rect(gameDisplay, (0, 0, 0), filled_rect)

surface = pygame.Surface([15, 15])      # wymiary kwadracika
surface.fill((225, 0, 0))               #czerwony
rectangle = surface.get_rect()

X = 60      #display coordinates   n * 88
Y = 680                         # 704 - m*88

x = 0   #coordinates
y = 0

rectangle.x = X         #położenie kwadracika
rectangle.y = Y
pygame.draw.rect(gameDisplay, (225, 0, 0), rectangle, 0)

for p in range(8):
    for t in range(8):
        if Board[p][t].occupied is 1:
            gameDisplay.blit(pionek, (19 + p * 88, 704 - t * 88 - 65))

marked = [-1, -1]           #nothing marked, value less than 0


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                if x is not 0:
                    x = x - 1
                    X = X - 88
            elif event.key == pygame.K_RIGHT:
                if x is not 7:
                    x = x + 1
                    X = X + 88
            elif event.key == pygame.K_DOWN:
                if y is not 0:
                    y = y - 1
                    Y = Y + 88
            elif event.key == pygame.K_UP:
                if y is not 7:
                    y = y + 1
                    Y = Y - 88
            elif event.key == pygame.K_SPACE:
                if Board[x][y].occupied is 1 or Board[x][y].occupied is 2:
                    if marked[0] < 0:
                        marked = [x, y]
                else:
                    if marked[0] > -1 and abs(marked[0] - x) == 1 and abs(marked[1] - y) == 1:
                        if Board[marked[0]][marked[1]].team is "black" and marked[1] - y is -1:
                            move(marked[0], marked[1], x, y)
                        elif Board[marked[0]][marked[1]].team is "red" and marked[1] - y is 1:
                            move(marked[0], marked[1], x, y)
                        marked = [-1, -1]
                    elif marked[0] > -1 and abs(marked[0] - x) == 2 and abs(marked[1] - y) == 2 and Board[int((marked[0] + x)/2)][int((marked[1] + y)/2)].team is not Board[marked[0]][marked[1]].team:  #bicie
                        Board[int((marked[0] + x) / 2)][int((marked[1] + y) / 2)].occupied = False
                        #print(statistics.mean([marked[0], x]))      #!!
                        move(marked[0], marked[1], x, y)
                        marked = [-1, -1]
                    else:
                        marked = [-1, -1]

            gameDisplay.blit(img, (0, 0))
            surface = pygame.Surface([15, 15])
            surface.fill((225, 0, 0))
            rectangle = surface.get_rect()
            rectangle.x = X
            rectangle.y = Y
            pygame.draw.rect(gameDisplay, (225, 0, 0), rectangle, 0)

            for p in range(8):
                for t in range(8):
                    if Board[p][t].occupied is 1:
                        gameDisplay.blit(pionek, (19 + p * 88, 704 - t * 88 - 65))      #damke tu dołożyć

    pygame.display.update()
    clock.tick(60)              #nw co to

pygame.quit()
sys.exit()



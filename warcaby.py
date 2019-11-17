import pygame
import sys
import statistics


class Field:
    occupied = 0  # 0 - field free        1 - regular pionek    2 - damka
    team = "black"


Board = [[Field() for x in range(8)] for y in range(8)]

Board[0][0].occupied = 1  # ustawianie pionków
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

'''Board[1][7].occupied = 1
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
Board[6][6].team = "red"'''

Board[1][5].occupied = 1
Board[1][5].team = "red"
Board[3][5].occupied = 1
Board[3][5].team = "red"
Board[5][5].occupied = 1
Board[5][5].team = "red"
Board[7][5].occupied = 2
Board[7][5].team = "red"


def move(w, l, W, L):
    Board[W][L].occupied = Board[w][l].occupied
    Board[w][l].occupied = 0
    Board[W][L].team = Board[w][l].team
    if Board[W][L].team == "black" and L == 7:
        Board[W][L].occupied = 2
        print("damka")
    elif Board[W][L].team == "red" and L == 0:
        Board[W][L].occupied = 2


# zeby lepiej wygladalo ale nie pyka coś
'''                                 
def handle_space(x, y, w, l):
    if Board[x][y].occupied == 1 or Board[x][y].occupied == 2:
        if w < 0:
            return [x, y]
    else:
        if w > -1 and abs(w - x) == 1 and abs(l - y) == 1:
            move(w, l, x, y)
            return [-1, -1]
        elif w > -1 and abs(w - x) == 2 and abs(l - y) == 2 and Board[int((l + x) / 2)][int((l + y) / 2)].team != Board[w][l].team:  # bicie
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

gameDisplay = pygame.display.set_mode((704, 704))  # 704 podzielne przez 8
pygame.display.set_caption('Warcaby')
clock = pygame.time.Clock()  # nw po co

img = pygame.image.load("board2.png")
pionek = pygame.image.load("pionek.png")
damka = pygame.image.load("damka.png")
pionekred = pygame.image.load("pionekred.png")

gameDisplay.blit(img, (0, 0))
running = True

# filled_rect = pygame.Rect(44, 660, 15, 15)
# pygame.draw.rect(gameDisplay, (0, 0, 0), filled_rect)

surface = pygame.Surface([15, 15])  # wymiary kwadracika
surface.fill((225, 0, 0))  # czerwony
rectangle = surface.get_rect()

X = 60  # display coordinates   n * 88
Y = 680  # 704 - m*88

x = 0  # coordinates
y = 0

pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
myfont = pygame.font.SysFont('Times New Roman', 13)

rectangle.x = X  # położenie kwadracika
rectangle.y = Y
pygame.draw.rect(gameDisplay, (225, 0, 0), rectangle, 0)


def board_draw():
    for p in range(8):  # display pionkis
        for t in range(8):
            if Board[p][t].occupied == 0:
                continue
            textsurface = myfont.render((str(Board[p][t].occupied) + Board[p][t].team), 1, (0, 0, 0))
            gameDisplay.blit(textsurface, (19 + p * 88, 704 - t * 88 - 65))
            '''if Board[p][t].occupied == 1:
                if Board[p][t].team == "black":
                    gameDisplay.blit(pionek, (19 + p * 88, 704 - t * 88 - 65))
                    gameDisplay.blit(textsurface, (19 + p * 88, 704 - t * 88 - 65))
    
                else:
                    gameDisplay.blit(pionekred, (19 + p * 88, 704 - t * 88 - 65))
            elif Board[p][t].occupied == 2:
                gameDisplay.blit(damka, (19 + p * 88, 704 - t * 88 - 65))
    '''


marked = [-1, -1]  # nothing marked, value less than 0


def check_available_moves(x, y):
    team = Board[x][y].team
    nums = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    moves = 0
    if Board[x][y].occupied == 1:
        for z in nums:
            if x + z[0] > 6 or \
                    y + z[1] > 6:
                continue
            if (Board[x + z[0]][y + z[1]].occupied != 0
                    and Board[x + z[0]][y + z[1]].team != team
                    and Board[x + 2 * z[0]][y + 2 * z[1]].occupied == 0):
                moves += 1
    elif Board[x][y].occupied == 2:
        for z in nums:
            base = z.copy()
            while 1 <= x + base[0] <= 6 and 1 <= y + base[1] <= 6:
                if (Board[x + base[0]][y + base[1]].occupied != 0
                        and Board[x + base[0]][y + base[1]].team != team
                        and Board[x + base[0] + z[0]][y + base[1] + z[1]].occupied == 0):
                    moves += 1
                    break
                elif Board[x + base[0]][y + base[1]].occupied != 0:
                    print("elo dla", base[0], base[1])
                    break
                print(base)
                base[0] += z[0]
                base[1] += z[1]
    return moves


board_draw()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x != 0:
                    x = x - 1
                    X = X - 88
            elif event.key == pygame.K_RIGHT:
                if x != 7:
                    x = x + 1
                    X = X + 88
            elif event.key == pygame.K_DOWN:
                if y != 0:
                    y = y - 1
                    Y = Y + 88
            elif event.key == pygame.K_UP:
                if y != 7:
                    y = y + 1
                    Y = Y - 88
            elif event.key == pygame.K_SPACE:
                if Board[x][y].occupied == 1 or Board[x][y].occupied == 2:
                    print(check_available_moves(x, y), x, y)
                    marked = [x, y]
                else:
                    if (marked[0] > -1 and
                            abs(marked[0] - x) == 1 and
                            abs(marked[1] - y) == 1 and
                            Board[marked[0]][marked[1]].occupied == 1):
                        # jeśli pion jest zaznaczony, a odległość == tylko 1 od nowego x,y ->
                        # -> przesuwamy sie na nowe pole
                        if Board[marked[0]][marked[1]].team == "black" and marked[1] - y == -1:
                            move(marked[0], marked[1], x, y)
                        elif Board[marked[0]][marked[1]].team == "red" and marked[1] - y == 1:
                            move(marked[0], marked[1], x, y)
                    elif (marked[0] > -1 and
                          abs(marked[0] - x) == 2 and
                          abs(marked[1] - y) == 2 and
                          Board[int((marked[0] + x) / 2)][int((marked[1] + y) / 2)].occupied != 0 and
                          Board[int((marked[0] + x) / 2)][int((marked[1] + y) / 2)].team
                          != Board[marked[0]][marked[1]].team):  # bicie
                        # jeśli pion jest zaznaczony, x,y odległe są o dwa pola od zaznaczenia,
                        # w sredniej arytmetycznej jest przeciwnik -> mozna bic
                        Board[int((marked[0] + x) / 2)][int((marked[1] + y) / 2)].occupied = 0
                        # print(statistics.mean([marked[0], x]))      #!!
                        move(marked[0], marked[1], x, y)

                    elif (marked[0] > -1 and
                          abs(marked[0] - x) == abs(marked[1] - y) and
                          Board[marked[0]][marked[1]].occupied == 2):
                        # jesli porusza sie po skosie i jest damka

                        marked_x = marked[0]
                        marked_y = marked[1]
                        x_is_increasing = False
                        y_is_increasing = False

                        if marked[0] > x:
                            marked_x -= 1
                        else:
                            x_is_increasing = True
                            marked_x += 1

                        if marked[1] > y:
                            marked_y -= 1
                        else:
                            marked_y += 1
                            y_is_increasing = True

                        is_a_piece = False
                        too_many_pieces = False
                        own_team = False
                        piece = [0, 0]
                        while marked_x != x:
                            if Board[marked_x][marked_y].occupied != 0:
                                if Board[marked_x][marked_y].team == Board[marked[0]][marked[1]].team:
                                    own_team = True
                                    print("swoj")
                                    break
                                elif is_a_piece:
                                    print("Too many", marked_x, marked_y)
                                    too_many_pieces = True
                                    break
                                is_a_piece = True
                                print("there is one", marked_x, marked_y)
                                piece = marked_x, marked_y
                            if x_is_increasing:
                                marked_x += 1
                            else:
                                marked_x -= 1
                            if y_is_increasing:
                                marked_y += 1
                            else:
                                marked_y -= 1

                        if not own_team:
                            if not is_a_piece:
                                move(marked[0], marked[1], x, y)
                            elif not too_many_pieces:
                                move(marked[0], marked[1], x, y)
                                Board[piece[0]][piece[1]].occupied = 0

                    marked = [-1, -1]

            gameDisplay.blit(img, (0, 0))
            surface = pygame.Surface([15, 15])
            surface.fill((225, 0, 0))
            rectangle = surface.get_rect()
            rectangle.x = X
            rectangle.y = Y
            pygame.draw.rect(gameDisplay, (225, 0, 0), rectangle, 0)

            board_draw()

    pygame.display.update()
    clock.tick(60)  # nw co to

pygame.quit()
sys.exit()

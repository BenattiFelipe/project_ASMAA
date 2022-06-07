import pygame






entry1 = [156, -23, 0, 0, 1, 'road1']
entry2 = [184, 401, 180, 0, -1, 'road2']
entry3 = [-23, 219, 90, 1, 0, 'road3']
entry4 = [-23, 256, 90, 1, 0]
entry5 = [-23, 284, 90, 1, 0]
entry6 = [-23, 313, 90, 1, 0]
entry7 = [1148, 124 , -90, -1, 0]
entry8 = [1148, 96 , -90, -1, 0]
entry9 = [1148, 154 , -90, -1, 0]

entry = entry3
#entry = [150, 150, 0, 0, 0]


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Cars Race')
icon = pygame.image.load('car.png')
pygame.display.set_icon(icon)

width,height = 1148,401
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('road.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

carImg = [pygame.image.load('car2.png')]
carX = entry[0]
carY = entry[1]
carImg[0] = pygame.transform.rotate(carImg[0], entry[2])
turning = 0

def car(x, y):
    screen.blit(carImg, (x, y))


def check_rotation(entry, carImg, x, y, turn):
    
    if turn[0] == 'road1' and y > turn[1]:
        entry[2] = turn[2]
        carImg[0] = pygame.transform.rotate(carImg[0], entry[2])
        if turn == turn1:
            entry[4] = 0
            entry[3] = 1
            entry[5] = 'road4'
        elif turn == turn2:
            entry[4] = 0
            entry[3] = -1
            entry[5] = 'road3'
        turn[0] = None
        screen.blit(carImg[0], (x, y))

    elif turn[0] == 'road2' and y < turn[1]:
        entry[2] = turn[2]
        carImg[0] = pygame.transform.rotate(carImg[0], entry[2]-180)
        if turn == turn3:
            entry[4] = 0
            entry[3] = 1
            entry[5] = 'road4'
        elif turn == turn4:
            entry[4] = 0
            entry[3] = -1
            entry[5] = 'road3'
        turn[0] = None
        screen.blit(carImg[0], (x, y))

    elif turn[0] == 'road3' and x > turn[1]:
        entry[2] = turn[2]
        carImg[0] = pygame.transform.rotate(carImg[0], entry[2]-90)
        if turn == turn5:
            entry[4] = 1
            entry[3] = 0
            entry[5] = 'road3'
        elif turn == turn6:
            entry[4] = -1
            entry[3] = 0
        turn[0] = None
        screen.blit(carImg[0], (x, y))

    else: 
        screen.blit(carImg[0], (x, y))
            

global turn1, turn2, turn3, turn4, turn5, turn6
turn1 = ['road1', 218, 90] # down to right
turn2 = ['road1', 190, -90] # down to left
turn3 = ['road2', 218, 90] # up to right
turn4 = ['road2', 190, 270] # up to left
turn5 = ['road3', 155, 0] # left to down 
turn6 = ['road3', 185, 180] # left to up 
turn = turn6

running = True
while running:
    window.blit(bg_img,(0,0))
    carX_change = 0.6*entry[3]
    carY_change = 0.6*entry[4]
    #entry[2] = 1
    #carImg = pygame.transform.rotate(carImg, entry[2])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    carX += carX_change
    carY += carY_change
    check_rotation(entry, carImg, carX, carY, turn)
    #car(carX, carY)
    pygame.display.update()
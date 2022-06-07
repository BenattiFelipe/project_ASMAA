import pygame

entry1 = [154, -31, 0, 0, 1]
entry2 = [181, 401, 180, 0, -1]
entry3 = [-31, 215, 90, 1, 0]
entry4 = [-31, 252, 90, 1, 0]
entry5 = [-31, 280, 90, 1, 0]
entry6 = [-31, 309, 90, 1, 0]
entry7 = [1148, 120 , -90, -1, 0]
entry8 = [1148, 92 , -90, -1, 0]
entry8 = [1148, 150 , -90, -1, 0]

entry = entry1


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Cars Race')
icon = pygame.image.load('car.png')
pygame.display.set_icon(icon)

width,height = 1148,401
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('road.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

carImg = pygame.image.load('car.png')
carX = entry[0]
carY = entry[1]
carImg = pygame.transform.rotate(carImg, entry[2])

def car(x, y):
    screen.blit(carImg, (x, y))

running = True
while running:
    window.blit(bg_img,(0,0))
    carX_change = 0.4*entry[3]
    carY_change = 0.4*entry[4]


    #Rotation!
    '''if carX == 154 and carY > 100 and entry[2] <= 45:
        entry[3] = 1
        entry[2] += 10
        rotated_image = pygame.transform.rotate(carImg, entry[2])
        #new_rect = rotated_image.get_rect(center = carImg.get_rect(center = (300, 300)).center)
        carImg = rotated_image'''


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    carX += carX_change
    carY += carY_change
    car(carX, carY)
    pygame.display.update()
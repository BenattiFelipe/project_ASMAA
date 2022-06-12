import pygame
from models import Car
import numpy as np
from static import *
import math

#['road1', 'road3', 'pass2', 'road8', 'road9', 'road10', 'road9', 'road8', 'pass4', 'road7', 'pass3', 'road8', 'pass4', 'road7', 'pass1', 'road4', 'road2']

#entry = [150, 150, 0, 0, 0]
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
carImg = []
for i in range(50):
    carImg.append(pygame.image.load('car2.png'))
for i in range(50):
    carImg[i] = pygame.transform.rotate(carImg[i], entry[2])
path = ['road3', 'road8', 'road9', 'road10', 'road9', 'road8', 'road7', 'road8', 'road7', 'road6', 'road5', 'road6', 'road7', 'road4', 'road2']
cars = []
for i in range(50):
    cars.append(Car('#car'+str(i),[entry[0], entry[1], entry[2], entry[5]], entry[3:5], ['road3', 'road8', 'road9', 'road10', 'road9', 'road8', 'road7', 'road8', 'road7', 'road6', 'road5', 'road6', 'road7', 'road4', 'road2'], carImg[i], 0, 0))


def vehicle(x, y, j):
    screen.blit(cars[j].figure, (x, y))

def explosion(x, y, j):
    screen.blit(explosions[j][2], (x, y))


def check_rotation(turn, car):
        #Rotation type 1: 
    if turn == turn1 and car.pos[1] > turn[1]:
        return rotation_type_1(turn, 0, 0, 1, 'road3', car)
    elif turn == turn2 and car.pos[1] > turn[1]:
        return rotation_type_1(turn, 0, 0, -1, 'road4', car)
    elif turn == turn3 and car.pos[1] < turn[1]:
        return rotation_type_1(turn, -180, 0, 1, 'road3', car)
    elif turn == turn4 and car.pos[1] < turn[1]:
        return rotation_type_1(turn, -180, 0, -1, 'road4', car)
    elif turn == turn5 and car.pos[0] > turn[1]:
        return rotation_type_1(turn, -90, 1, 0, 'road1', car)
    elif turn == turn6 and car.pos[0] > turn[1]:
        return rotation_type_1(turn, -90, -1, 0, 'road2', car)
    elif turn == turn7 and car.pos[0] < turn[1]:
        return rotation_type_1(turn, 90, 1, 0, 'road1', car)
    elif turn == turn8 and car.pos[0] < turn[1]:
        return rotation_type_1(turn, 90, -1, 0, 'road2', car)
    #Rotation type 2:
    elif turn == turn9 and (car.pos[0] > turn[0][1] or car.pos[1] > turn[1][1]):
        turn =  rotation_type_2(turn, 0, -90, 1, 0, 0, 1, 'road8', car)
    elif turn == turn14 and (car.pos[0] > turn[0][1] or car.pos[1] < turn[1][1]):
        return rotation_type_2(turn, -180, -90, -1, 0, 0, -1, 'road7', car)
    elif turn == turn19 and (car.pos[0] < turn[0][1] or car.pos[1] > turn[1][1]):
        return rotation_type_2(turn, -180, -90, 1, 0, 0, 1, 'road8', car)
    elif turn == turn20 and (car.pos[0] < turn[0][1] or car.pos[1] > turn[1][1]):
        return rotation_type_2(turn, -180, 90, -1, 0, 0, 1, 'road4', car)
    elif turn == turn21 and (car.pos[0] < turn[0][1] or car.pos[1] > turn[1][1]):
        return rotation_type_2(turn, 0, 90, -1, 0, 0, 1, 'road5', car)
    elif turn == turn22 and (car.pos[0] > turn[0][1] or car.pos[1]  < turn[1][1]):
        return rotation_type_2(turn, 0, -90, 1, 0, 0, -1, 'road10', car)
    #Transition
    elif turn == turn10 or turn == turn11 or turn == turn12 or turn == turn13 or turn == turn15 or turn == turn16 or turn == turn17 or turn == turn18:
        if turn == turn10:
            car.pos[1] += 30
            car.pos[3] = 'road9'
        elif turn == turn11:
            car.pos[1] += 30
            car.pos[3] = 'road10'
        elif turn == turn12:
            car.pos[1] -= 30
            car.pos[3] = 'road9'
        elif turn == turn13:
            car.pos[1] -= 30
            car.pos[3] = 'road8'
        elif turn == turn15:
            car.pos[1] -= 30
            car.pos[3] = 'road6'
        elif turn == turn16:
            car.pos[1] -= 30
            car.pos[3] = 'road5'
        elif turn == turn17:
            car.pos[1] += 30
            car.pos[3] = 'road6'
        elif turn == turn18:
            car.pos[1] += 30
            car.pos[3] = 'road7'
        del car.intentions[0]
        turn = define_rotation(car)
        return turn

    return turn
def rotation_type_1(turn, rot, vel_x, vel_y, new_road, car):
    print(turn)
    car.pos[2] = turn[2]
    car.figure = pygame.transform.rotate(car.figure, car.pos[2] + rot)
    car.vel[1] = vel_x
    car.vel[0] = vel_y
    car.pos[3] = new_road
    del car.intentions[0]
    return define_rotation(car)

def rotation_type_2(turn, rot1, rot2, vel_x1, vel_y1, vel_x2, vel_y2, new_road, car):
    print(turn)
    if (car.pos[1] > turn[1][1] and (turn == turn9 or turn == turn19 or turn == turn20 or turn == turn21)) or (car.pos[1] < turn[1][1] and (turn == turn14 or turn == turn22)):
        car.pos[2] = turn[1][2]
        car.figure = pygame.transform.rotate(car.figure, car.pos[2] + rot1)
        car.vel[1] = vel_y1
        car.vel[0] = vel_x1
        car.pos[3] = new_road
        del car.intentions[0]
        return define_rotation(car)
    elif car.pos[2] != turn[0][2]:
        car.pos[2] = turn[0][2]
        car.figure = pygame.transform.rotate(car.figure, car.pos[2] + rot2)
        car.vel[1] = vel_y2
        car.vel[0] = vel_x2
    return turn
    
def isCollision(x1, x2, y1, y2, size_x, size_y):
    distance_x = abs(x1 - x2)
    distance_y = abs(y1 - y2)
    return distance_x <= size_x and distance_y <= size_y
        

def define_rotation(car):
    if car.intentions == []:
        return None
    elif car.intentions[0] == 'road3' and car.pos[3] == 'road1':
        turn = turn1
    elif car.intentions[0] == 'road4' and car.pos[3] == 'road1':
        turn = turn2
    elif car.intentions[0] == 'road3' and car.pos[3] == 'road2':
        turn = turn3
    elif car.intentions[0] == 'road4' and car.pos[3] == 'road2':
        turn = turn4
    elif car.intentions[0] == 'road1' and car.pos[3] == 'road3':
        turn = turn5
    elif car.intentions[0] == 'road2' and car.pos[3] == 'road3':
        turn = turn6
    elif car.intentions[0] == 'road1' and car.pos[3] == 'road4':
        turn = turn7
    elif car.intentions[0] == 'road2' and car.pos[3] == 'road4':
        turn = turn8
    elif car.intentions[0] == 'road8' and car.pos[3] == 'road3':
        turn = turn9
    elif car.intentions[0] == 'road9' and car.pos[3] == 'road8':
        turn = turn10
    elif car.intentions[0] == 'road10' and car.pos[3] == 'road9':
        turn = turn11
    elif car.intentions[0] == 'road9' and car.pos[3] == 'road10':
        turn = turn12
    elif car.intentions[0] == 'road8' and car.pos[3] == 'road9':
        turn = turn13
    elif car.intentions[0] == 'road7' and car.pos[3] == 'road8' and car.pos[0] < 785:
        turn = turn14 
    elif car.intentions[0] == 'road6' and car.pos[3] == 'road7':
        turn = turn15
    elif car.intentions[0] == 'road5' and car.pos[3] == 'road6':
        turn = turn16
    elif car.intentions[0] == 'road6' and car.pos[3] == 'road5':
        turn = turn17
    elif car.intentions[0] == 'road7' and car.pos[3] == 'road6':
        turn = turn18
    elif car.intentions[0] == 'road8' and car.pos[3] == 'road7' and car.pos[0] > 640:
        turn = turn19
    elif car.intentions[0] == 'road4' and car.pos[3] == 'road7' and car.pos[0] > 200:
        turn = turn20
    elif car.pos[3] == 'entry1':
        turn = turn21
    elif car.pos[3] == 'entry2':
        turn = turn22
    else:
        turn = None

    return turn
count = [0 for i in range(len(cars))]
turn = [define_rotation(cars[j]) for j in range(len(cars))]
inside = [cars[0]]    
running = True
i = 0
k = 0
explosions = []
while running:
    i += 1
    if i == 100:
        i = 0
        inside.append(cars[k])
        k += 1
    window.blit(bg_img,(0,0))
    delete = []
    for j in range(len(inside)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        carX_change = 0.3*cars[j].vel[0]
        carY_change = 0.3*cars[j].vel[1]
        #entry[2] = 1
        #carImg = pygame.transform.rotate(carImg, entry[2])
        
        cars[j].pos[0] += carX_change
        cars[j].pos[1] += carY_change
        if count[j] == 0 or count[j] > 100:
            turn[j] = check_rotation(turn[j], cars[j])
            count[j] = 0
        if count[j] > 0:

            count[j] += 1
        if (turn[j] == turn10 or turn[j] == turn11 or turn[j] == turn12 or turn[j] == turn13 or turn[j] == turn15 or turn[j] == turn16 or turn[j] == turn17 or turn[j] == turn18) and count[j] == 0:
            count[j] = 1
        for m in range(len(inside)):
            if cars[m] != cars[j]:            
                if isCollision(cars[j].pos[0], cars[m].pos[0], cars[j].pos[1], cars[m].pos[1], 16, 16):
                    explosions.append([(cars[j].pos[0] + cars[m].pos[0])/2, (cars[j].pos[1] + cars[m].pos[1])/2, pygame.image.load('bang.png'), 0])
                    if cars[m] not in delete:
                        delete.append(cars[m])
                    if cars[j] not in delete:
                        delete.append(cars[j])
        
        vehicle(cars[j].pos[0], cars[j].pos[1], j)
    for m in range(len(explosions)):
        if explosions[m][3] <= 20:
            explosions[m][3] += 1
            explosion(explosions[m][0], explosions[m][1], m)
        #else:
            #del explosions[m]
    #delete = reversed(sorted(delete))
    for value in delete:
        inside2 = []
        for carro in inside:
            if carro.name != value.name:
                inside2.append(carro)
        inside = inside2
        car2 = []
        for carro in cars:
            if carro.name != value.name:
                car2.append(carro)
        cars = car2
        print(inside[0].intentions)
        
        #car(carX, carY)
    pygame.display.update()
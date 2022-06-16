import pygame
from models import Car, System, Cross
import numpy as np
from static import *
import math
import random
from datetime import datetime

#['road1', 'road3', 'pass2', 'road8', 'road9', 'road10', 'road9', 'road8', 'pass4', 'road7', 'pass3', 'road8', 'pass4', 'road7', 'pass1', 'road4', 'road2']

#entry = [150, 150, 0, 0, 0]
entry = entry8

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
up_road = pygame.image.load('uper_road.png')
up_road = pygame.transform.scale(up_road,(50,278))
system = System()
for i in range(200):
    carImg.append(pygame.image.load('car2.png'))
#for i in range(200):
    #carImg[i] = pygame.transform.rotate(carImg[i], entry[2])
path = ['road3', 'road8', 'road9', 'road10', 'road9', 'road8', 'road7', 'road8', 'road7', 'road6', 'road5', 'road6', 'road7', 'road4', 'road2']
cars = []
for i in range(200):
    entry = define_entry(entries)
    exit = define_exit(entry)
    position = define_position(entry)
    direction = define_velocity(entry)
    intentions = []
    if entry == entry10:
        intentions.append('road5')
    if entry == entry11:
        intentions.append('road10')
    cars.append(Car( system, 'car#' + str(i), position, direction, random.randint(30, 50), intentions, pygame.transform.rotate(carImg[i], position[2]),[24,12], 0, 0, datetime.now, entry, exit))


def upper_road(x, y):
    screen.blit(up_road, (x, y))

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
    elif turn == turn23 and (car.pos[0] > turn[0][1] or car.pos[1]  > turn[1][1]):
        return rotation_type_2(turn, 180, 90, 1, 0, 0, 1, 'out1', car)
    elif turn == turn24 and (car.pos[0] < turn[0][1] or car.pos[1] < turn[1][1]):
        return rotation_type_2(turn, 180, 90, -1, 0, 0,-1, 'out2', car)
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

    car.pos[2] = turn[2]
    car.figure = pygame.transform.rotate(car.figure, car.pos[2] + rot)
    car.direction[1] = vel_x
    car.direction[0] = vel_y
    car.pos[3] = new_road
    del car.intentions[0]
    return define_rotation(car)

def rotation_type_2(turn, rot1, rot2, vel_x1, vel_y1, vel_x2, vel_y2, new_road, car):

    if (car.pos[1] > turn[1][1] and (turn == turn9 or turn == turn19 or turn == turn20 or turn == turn21 or turn == turn23)) or (car.pos[1] < turn[1][1] and (turn == turn14 or turn == turn22 or turn == turn24)):
        car.pos[2] = turn[1][2]
        car.figure = pygame.transform.rotate(car.figure, car.pos[2] + rot1)
        car.direction[1] = vel_y1
        car.direction[0] = vel_x1
        car.pos[3] = new_road
        del car.intentions[0]
        return define_rotation(car)
    elif car.pos[2] != turn[0][2]:
        car.pos[2] = turn[0][2]
        car.figure = pygame.transform.rotate(car.figure, car.pos[2] + rot2)
        car.direction[1] = vel_y2
        car.direction[0] = vel_x2
        if turn == turn19:
            car.pos[3] = 'return1'
        if turn == turn14:
            car.pos[3] = 'return2'
    return turn
    
def isCollision(x1, x2, y1, y2, size_x, size_y, position1, position2):
    set =  ['road1', 'road2'] 
    if (position1 in set and position2 not in set) or (position1 not in set and position2 in set):
        return False
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
    elif car.intentions[0] == 'road7' and (car.pos[3] == 'road8' or car.pos[3] ==  'return2'):
        turn = turn14 
    elif car.intentions[0] == 'road6' and car.pos[3] == 'road7':
        turn = turn15
    elif car.intentions[0] == 'road5' and car.pos[3] == 'road6':
        turn = turn16
    elif car.intentions[0] == 'road6' and car.pos[3] == 'road5':
        turn = turn17
    elif car.intentions[0] == 'road7' and car.pos[3] == 'road6':
        turn = turn18
    elif car.intentions[0] == 'road8' and (car.pos[3] == 'road7' or car.pos[3] == 'return1'):
        turn = turn19
    elif car.intentions[0] == 'road4' and car.pos[3] == 'road7' and car.pos[0] > 200:
        turn = turn20
    elif car.pos[3] == 'entry1':
        turn = turn21
    elif car.pos[3] == 'entry2':
        turn = turn22
    elif car.intentions[0] == 'out1' and car.pos[3] == 'road10':
        turn = turn23
    elif car.intentions[0] == 'out2' and car.pos[3] == 'road5':
        turn = turn24
    else:
        turn = None

    return turn
    

for car in cars:
    car.turn = define_rotation(car)
inside = [cars[0]]   
running = True
cross = Cross()
i = 0
k = 1

explosions = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    i += 1
    bool = True
    if i == 50:
        i = 0
        inside.append(cars[k])
        k += 1
    window.blit(bg_img,(0,0))
    delete = []
    render = []
    cross.define_next(inside)
    for j in range(len(inside)):


        carX_change = (1/50)*inside[j].vel*inside[j].direction[0]
        carY_change = (1/50)*inside[j].vel*inside[j].direction[1]

        inside[j].pos[0] += carX_change
        inside[j].pos[1] += carY_change


        if (inside[j].pos[1] == 55 and inside[j].pos[0] < 876) or (inside[j].pos[0] < 300 and inside[j].pos[3] == 'road5' and inside[j].exit[1] == 'out2') or (inside[j].pos[3] == 'road7' and inside[j].pos[0] < 640) or (inside[j].pos[3] == 'road8' and inside[j].pos[0] > 785) or (inside[j].pos[1] == 355 and inside[j].pos[0] > 544) or (inside[j].pos[0] > 899 and inside[j].pos[3] == 'road10' and inside[j].exit[1] == 'out1') :
            inside[j].turn = define_rotation(inside[j])

            if inside[j].turn == turn19:
                contador = 0
                for car in inside:
                    if car.pos[3] == 'return1':
                        contador += 1
                if contador > 0:
                    inside[j].give_up = True
            if inside[j].turn == turn14:
                contador = 0
                for car in inside:
                    if car.pos[3] == 'return2':
                        contador += 1
                if contador > 0:
                    inside[j].give_up = True
            if not inside[j].give_up:
                check_rotation(inside[j].turn, inside[j])
        if inside[j].give_up:
            inside[j].make_decision_free_road()
        if inside[j].pos[3] not in ['road1', 'road2', 'road3', 'road4']:

            inside[j].detect_car(inside[j].size[0]*7, inside)
            action = inside[j].make_decision_free_road()

            if action == 'is out':
                delete.append(inside[j])
            if action == 'change lane' or action == 'get out':
                inside[j].turn = define_rotation(inside[j])
                check_rotation(inside[j].turn, inside[j])  
        
        else:
            inside[j].detect_car(inside[j].size[0]*7, inside)
            action = inside[j].make_decision_cross()
            inside[j].turn = define_rotation(inside[j])
            check_rotation(inside[j].turn, inside[j])
            if action == 'is out':
                delete.append(inside[j])

        '''if inside[j].count > 0:
            inside[j].count += 1
        if (inside[j].turn == turn10 or inside[j].turn == turn11 or inside[j].turn == turn12 or inside[j].turn == turn13 or inside[j].turn == turn15 or inside[j].turn == turn16 or inside[j].turn == turn17 or inside[j].turn == turn18) and inside[j].count == 0:
            inside[j].count = 1
        if inside[j].count == 0 or inside[j].count > 100:
            inside[j].count = 0'''
            
        for m in range(len(inside)):
            if inside[m] != inside[j]:            
                if isCollision(inside[j].pos[0], inside[m].pos[0], inside[j].pos[1], inside[m].pos[1], 16, 16, inside[j].pos[3], inside[m].pos[3]):
                    explosions.append([(inside[j].pos[0] + inside[m].pos[0])/2, (inside[j].pos[1] + inside[m].pos[1])/2, pygame.image.load('bang.png'), 0])
                    if inside[m] not in delete:
                        delete.append(inside[m])
                    if inside[j] not in delete:
                        delete.append(inside[j])
        if inside[j].pos[3] not in ['road1', 'road2', 'road3', 'road4']:
            render.append([inside[j], j, True])
        else:
            render.append([inside[j], j, False])
        
    
    
    for value in render:
        if value[2] == True:
            vehicle(value[0].pos[0], value[0].pos[1], value[1])
    upper_road(158, 80)
    for value in render:
        if value[2] == False:
            vehicle(value[0].pos[0], value[0].pos[1], value[1])
    for m in range(len(explosions)):
        if explosions[m][3] <= 20:
            explosions[m][3] += 1
            explosion(explosions[m][0], explosions[m][1], m)
        #else:
            #del explosions[m]
    #delete = reversed(sorted(delete))

    for value in delete:
        k -= 1
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
    pygame.display.update()
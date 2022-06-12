from static import *
import pygame

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


def rotation_type_1(turn, rot, vel_x, vel_y, new_road, car):
    print(turn)
    car.pos[2] = turn[2]
    car.figure = pygame.transform.rotate(car.figure, car.pos[2] + rot)
    car.vel[1] = vel_x
    car.vel[0] = vel_y
    car.pos[3] = new_road
    del car.intentions[0]


def rotation_type_2(turn, rot1, rot2, vel_x1, vel_y1, vel_x2, vel_y2, new_road, car):

    if (car.pos[1] > turn[1][1] and (turn == turn9 or turn == turn19 or turn == turn20 or turn == turn21)) or (car.pos[1] < turn[1][1] and (turn == turn14 or turn == turn22)):
        car.pos[2] = turn[1][2]
        car.figure = pygame.transform.rotate(car.figure, car.pos[2] + rot1)
        car.vel[1] = vel_y1
        car.vel[0] = vel_x1
        car.pos[3] = new_road
        del car.intentions[0]

    elif car.pos[2] != turn[0][2]:
        car.pos[2] = turn[0][2]
        car.figure = pygame.transform.rotate(car.figure, car.pos[2] + rot2)
        car.vel[1] = vel_y2
        car.vel[0] = vel_x2

    
            
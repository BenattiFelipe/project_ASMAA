import pygame



class Car:
    def __init__(self,pos,vel, intentions, figure):
        #self.name = name
        self.pos = pos
        self.vel = vel
        self.intentions = intentions
        self.figure = figure
        #self.accel = accel
        #self.size = size
    
    #def move(self, dt):
        #self.vel += self.accel*dt


entry1 = [156, -23, 0, 0, 1, 'road1']
entry2 = [184, 401, 180, 0, -1, 'road2']
entry3 = [-23, 219, 90, 1, 0, 'road3']
entry4 = [-23, 256, 90, 1, 0]
entry5 = [-23, 284, 90, 1, 0]
entry6 = [-23, 313, 90, 1, 0]
entry7 = [1148, 124 , -90, -1, 0]
entry8 = [1148, 96 , -90, -1, 0]
entry9 = [1148, 154 , -90, -1, 0]
entry10 = [930, 55, -90, -1, 0, 'entry1']
entry11 = [490, 355, 90, 1, 0, 'entry2']

entry = entry11

#['road1', 'road3', 'pass2', 'road8', 'road9', 'road10', 'road9', 'road8', 'pass4', 'road7', 'pass3', 'road8', 'pass4', 'road7', 'pass1', 'road4', 'road2']

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
carImg[0] = pygame.transform.rotate(carImg[0], entry[2])
car_1 = Car([entry[0], entry[1], entry[2], entry[5]], entry[3:5], ['road3', 'road8', 'road9', 'road10', 'road9', 'road8', 'road7', 'road8', 'road7', 'road6', 'road5', 'road6', 'road7', 'road4', 'road2'], carImg[0])


def check_rotation(x, y, turn):
    if turn == None: 
        screen.blit(car_1.figure, (x, y))

    elif turn[0] == 'road1' and y > turn[1]:
        car_1.pos[2] = turn[2]
        car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2])
        if turn == turn1:
            car_1.vel[1] = 0
            car_1.vel[0] = 1
            car_1.pos[3] = 'road3'
        elif turn == turn2:
            car_1.vel[1] = 0
            car_1.vel[0] = -1
            car_1.pos[3] = 'road4'
        del car_1.intentions[0]
        turn = define_rotation()
        screen.blit(car_1.figure, (x, y))
        

    elif turn[0] == 'road2' and y < turn[1]:
        car_1.pos[2] = turn[2]
        car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2]-180)
        if turn == turn3:
            car_1.vel[1] = 0
            car_1.vel[0] = 1
            car_1.pos[3] = 'road3'
        elif turn == turn4:
            car_1.vel[1] = 0
            car_1.vel[0] = -1
            car_1.pos[3] = 'road4'
        del car_1.intentions[0]
        turn = define_rotation()
        screen.blit(car_1.figure, (x, y))

    elif turn[0] == 'road3' and x > turn[1]:
        car_1.pos[2] = turn[2]
        car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2] -90)
        if turn == turn5:
            car_1.vel[1] = 1
            car_1.vel[0] = 0
            car_1.pos[3] = 'road1'
        elif turn == turn6:
            car_1.vel[1] = -1
            car_1.vel[0] = 0
            car_1.pos[3] = 'road2'
        del car_1.intentions[0]
        turn = define_rotation()
        screen.blit(car_1.figure, (x, y))

    elif turn[0] == 'road4' and x < turn[1]:
        car_1.pos[2] = turn[2]
        car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2] +90)
        if turn == turn7:
            car_1.vel[1] = 1
            car_1.vel[0] = 0
            car_1.pos[3] = 'road1'
        elif turn == turn8:
            car_1.vel[1] = -1
            car_1.vel[0] = 0
            car_1.pos[3] = 'road2'
        del car_1.intentions[0]
        turn = define_rotation()
        screen.blit(car_1.figure, (x, y))

    elif turn == turn9 and (x > turn[0][1] or y > turn[1][1]):
        if y > turn[1][1]:
            car_1.pos[2] = turn[1][2]
            car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2])
            car_1.vel[1] = 0
            car_1.vel[0] = 1
            car_1.pos[3] = 'road8'
            del car_1.intentions[0]
            turn = define_rotation()
            screen.blit(car_1.figure, (x, y))
        elif car_1.pos[2] != turn[0][2]:
            car_1.pos[2] = turn[0][2]
            car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2] -90)
            car_1.vel[1] = 1
            car_1.vel[0] = 0
            car_1.pos[3] = 'road3'
            screen.blit(car_1.figure, (x, y))
        else:
            screen.blit(car_1.figure, (x, y))
    elif turn == turn10 or turn == turn11 or turn == turn12 or turn == turn13 or turn == turn15 or turn == turn16 or turn == turn17 or turn == turn18:
        if turn == turn10:
            car_1.pos[1] += 30
            car_1.pos[3] = 'road9'
        elif turn == turn11:
            car_1.pos[1] += 30
            car_1.pos[3] = 'road10'
        elif turn == turn12:
            car_1.pos[1] -= 30
            car_1.pos[3] = 'road9'
        elif turn == turn13:
            car_1.pos[1] -= 30
            car_1.pos[3] = 'road8'
        elif turn == turn15:
            car_1.pos[1] -= 30
            car_1.pos[3] = 'road6'
        elif turn == turn16:
            car_1.pos[1] -= 30
            car_1.pos[3] = 'road5'
        elif turn == turn17:
            car_1.pos[1] += 30
            car_1.pos[3] = 'road6'
        elif turn == turn18:
            car_1.pos[1] += 30
            car_1.pos[3] = 'road7'
        del car_1.intentions[0]
        turn = define_rotation()
        screen.blit(car_1.figure, (car_1.pos[0], car_1.pos[1]))
    elif turn == turn14 and (x > turn[0][1] or y < turn[1][1]):
        if y < turn[1][1]:
            car_1.pos[2] = turn[1][2]
            car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2]-180)
            car_1.vel[1] = 0
            car_1.vel[0] = -1
            car_1.pos[3] = 'road7'
            del car_1.intentions[0]
            turn = define_rotation()
            screen.blit(car_1.figure, (x, y))
        elif car_1.pos[2] != turn[0][2]:
            car_1.pos[2] = turn[0][2]
            car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2] -90)
            car_1.vel[1] = -1
            car_1.vel[0] = 0
            car_1.pos[3] = 'road8'
            screen.blit(car_1.figure, (x, y))
        else:
            screen.blit(car_1.figure, (x, y))
    elif turn == turn19 and (x < turn[0][1] or y > turn[1][1]):
        if y > turn[1][1]:
            car_1.pos[2] = turn[1][2]
            car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2]-180)
            car_1.vel[1] = 0
            car_1.vel[0] = 1
            car_1.pos[3] = 'road8'
            del car_1.intentions[0]
            turn = define_rotation()
            screen.blit(car_1.figure, (x, y))
        elif car_1.pos[2] != turn[0][2]:
            car_1.pos[2] = turn[0][2]
            car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2] -90)
            car_1.vel[1] = 1
            car_1.vel[0] = 0
            car_1.pos[3] = 'road7'
            screen.blit(car_1.figure, (x, y))
        else:
            screen.blit(car_1.figure, (x, y))
    elif turn == turn20 and (x < turn[0][1] or y > turn[1][1]):
        if y > turn[1][1]:
            car_1.pos[2] = turn[1][2]
            car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2]-180)
            car_1.vel[1] = 0
            car_1.vel[0] = -1
            car_1.pos[3] = 'road4'
            del car_1.intentions[0]
            turn = define_rotation()
            screen.blit(car_1.figure, (x, y))
        elif car_1.pos[2] != turn[0][2]:
            car_1.pos[2] = turn[0][2]
            car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2] +90)
            car_1.vel[1] = 1
            car_1.vel[0] = 0
            car_1.pos[3] = 'road7'
            screen.blit(car_1.figure, (x, y))
        else:
            screen.blit(car_1.figure, (x, y))
    
    elif turn == turn21 and (x < turn[0][1] or y > turn[1][1]):
        if y > turn[1][1]:
            car_1.pos[2] = turn[1][2]
            car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2])
            car_1.vel[1] = 0
            car_1.vel[0] = -1
            car_1.pos[3] = 'road5'
            turn = define_rotation()
            screen.blit(car_1.figure, (x, y))
        elif car_1.pos[2] != turn[0][2]:
            car_1.pos[2] = turn[0][2]
            car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2] +90)
            car_1.vel[1] = 1
            car_1.vel[0] = 0
            car_1.pos[3] = 'road5'
            screen.blit(car_1.figure, (x, y))
        else:
            screen.blit(car_1.figure, (x, y))
    elif turn == turn22 and (x > turn[0][1] or y < turn[1][1]):
        if y < turn[1][1]:
            car_1.pos[2] = turn[1][2]
            car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2])
            car_1.vel[1] = 0
            car_1.vel[0] = 1
            car_1.pos[3] = 'road10'
            turn = define_rotation()
            screen.blit(car_1.figure, (x, y))
        elif car_1.pos[2] != turn[0][2]:
            car_1.pos[2] = turn[0][2]
            car_1.figure = pygame.transform.rotate(car_1.figure, car_1.pos[2] -90)
            car_1.vel[1] = -1
            car_1.vel[0] = 0
            car_1.pos[3] = 'road10'
            screen.blit(car_1.figure, (x, y))
        else:
            screen.blit(car_1.figure, (x, y))
    else: 
        screen.blit(car_1.figure, (x, y))
    return turn
            

global turn1, turn2, turn3, turn4, turn5, turn6, turn7, turn8, turn9, turn10, turn11, turn12, turn13, turn14, turn15, turn16, turn17, turn18, turn19, turn20, turn21, turn22, count
turn1 = ['road1', 218, 90] # down to right
turn2 = ['road1', 190, -90] # down to left
turn3 = ['road2', 218, 90] # up to right
turn4 = ['road2', 190, 270] # up to left
turn5 = ['road3', 155, 0] # left to down 
turn6 = ['road3', 185, 180] # left to up 
turn7 = ['road4', 155, 0]
turn8 = ['road4', 185, 180]
turn9 = [['road3', 406, 0], ['road3', 255, 90]]
turn10 = ['road8']
turn11 = ['road9']
turn12 = ['turn12']
turn13 = ['turn13']
turn14 = [['road8', 785, 180], ['road8', 155, -90]]
turn15 = ['turn15']
turn16 = ['turn16']
turn17 = ['turn17']
turn18 = ['turn18']
turn19 = [['road7', 640, 180], ['road7', 255, -90]]
turn20 = [['road7', 406, 0], ['road7', 190, 90]]
turn21 = [['road5', 887, 0], ['road5', 95, -90]]
turn22 = [['road10', 530, 180], ['road10', 315, -90]]

def define_rotation():
    if car_1.intentions == []:
        return None
    elif car_1.intentions[0] == 'road3' and car_1.pos[3] == 'road1':
        turn = turn1
    elif car_1.intentions[0] == 'road4' and car_1.pos[3] == 'road1':
        turn = turn2
    elif car_1.intentions[0] == 'road3' and car_1.pos[3] == 'road2':
        turn = turn3
    elif car_1.intentions[0] == 'road4' and car_1.pos[3] == 'road2':
        turn = turn4
    elif car_1.intentions[0] == 'road1' and car_1.pos[3] == 'road3':
        turn = turn5
    elif car_1.intentions[0] == 'road2' and car_1.pos[3] == 'road3':
        turn = turn6
    elif car_1.intentions[0] == 'road1' and car_1.pos[3] == 'road4':
        turn = turn7
    elif car_1.intentions[0] == 'road2' and car_1.pos[3] == 'road4':
        turn = turn8
    elif car_1.intentions[0] == 'road8' and car_1.pos[3] == 'road3':
        turn = turn9
    elif car_1.intentions[0] == 'road9' and car_1.pos[3] == 'road8':
        count[0] = 1
        turn = turn10
    elif car_1.intentions[0] == 'road10' and car_1.pos[3] == 'road9':
        count[0] = 1
        turn = turn11
    elif car_1.intentions[0] == 'road9' and car_1.pos[3] == 'road10':
        count[0] = 1
        turn = turn12
    elif car_1.intentions[0] == 'road8' and car_1.pos[3] == 'road9':
        count[0] = 1
        turn = turn13
    elif car_1.intentions[0] == 'road7' and car_1.pos[3] == 'road8' and car_1.pos[0] < 785:
        turn = turn14 
    elif car_1.intentions[0] == 'road6' and car_1.pos[3] == 'road7':
        count[0] = 1
        turn = turn15
    elif car_1.intentions[0] == 'road5' and car_1.pos[3] == 'road6':
        count[0] = 1
        turn = turn16
    elif car_1.intentions[0] == 'road6' and car_1.pos[3] == 'road5':
        count[0] = 1
        turn = turn17
    elif car_1.intentions[0] == 'road7' and car_1.pos[3] == 'road6':
        count[0] = 1
        turn = turn18
    elif car_1.intentions[0] == 'road8' and car_1.pos[3] == 'road7' and car_1.pos[0] > 640:
        turn = turn19
    elif car_1.intentions[0] == 'road4' and car_1.pos[3] == 'road7' and car_1.pos[0] > 200:
        turn = turn20
    elif car_1.pos[3] == 'entry1':
        turn = turn21
    elif car_1.pos[3] == 'entry2':
        turn = turn22
    else:
        turn = None

    return turn
count = [0]
turn = define_rotation()
running = True
while running:
    window.blit(bg_img,(0,0))
    carX_change = 0.2*car_1.vel[0]
    carY_change = 0.2*car_1.vel[1]
    #entry[2] = 1
    #carImg = pygame.transform.rotate(carImg, entry[2])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    car_1.pos[0] += carX_change
    car_1.pos[1] += carY_change
    if count[0] == 0 or count[0] > 100:
        turn = check_rotation(car_1.pos[0], car_1.pos[1], turn)
    if count[0] > 0:
        screen.blit(car_1.figure, (car_1.pos[0], car_1.pos[1]))
        count[0] += 1
    #car(carX, carY)
    pygame.display.update()
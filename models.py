import math
from static import speed_limit

class System:
    def __init__(self):
        self.entry1 = 'Empty'
    def check_empty(self, cars):
        self.entry1 = 'Empty'
        for car in cars:
            if car.pos[3] == 'entry1':
                self.entry1 = 'Full'
                break


def allowed_crosses(car_1, car_2):
    if (car_1.pos[3] == 'road1' and car_2.pos[3] == 'road2'):
        if (car_1.intentions in [[], ['road4']] and car_2.intentions in [[], ['road3']]):
            return True
    elif (car_1.pos[3] == 'road2' and car_2.pos[3] == 'road1'):
        if (car_1.intentions in [[], ['road3']] and car_2.intentions in [[], ['road4']]):
            return True
    elif (car_1.pos[3] == 'road1' and car_2.pos[3] == 'road3'):
        if (car_1.intentions == ['road4']):
            return True
    elif (car_1.pos[3] == 'road3' and car_2.pos[3] == 'road1'):
        if (car_2.intentions == ['road4']):
            return True
    elif (car_1.pos[3] == 'road1' and car_2.pos[3] == 'road4'):
        if (car_2.intentions == ['road2']):
            return True
    elif (car_1.pos[3] == 'road4' and car_2.pos[3] == 'road1'):
        if (car_1.intentions == ['road2']):
            return True
    elif (car_1.pos[3] == 'road2' and car_2.pos[3] == 'road3'):
        if (car_2.intentions == ['road1']):
            return True
    elif (car_1.pos[3] == 'road3' and car_2.pos[3] == 'road2'):
        if (car_1.intentions == ['road1']):
            return True
    elif (car_1.pos[3] == 'road2' and car_2.pos[3] == 'road4'):
        if (car_1.intentions == ['road3']):
            return True
    elif (car_1.pos[3] == 'road4' and car_2.pos[3] == 'road2'):
        if (car_2.intentions == ['road3']):
            return True
    elif (car_1.pos[3] == 'road3' and car_2.pos[3] == 'road4'):
        if (car_1.intentions in [[], ['road1']] and car_2.intentions in [[], ['road2']]):
            return True
    elif (car_1.pos[3] == 'road4' and car_2.pos[3] == 'road3'):
        if (car_1.intentions in [[], ['road2']] and car_2.intentions in [[], ['road1']]):
            return True


class Cross:
    def __init__(self):
        self.roads = ['road1', 'road2', 'road3', 'road4']
    def check_cross(self, system):
        for car in system:
            if car.pos[0] > 130 and car.pos[0] < 210 and car.pos[1] > 165 and car.pos[1] < 245:
                return True
    def define_next(self, system):
        if self.check_cross(system):
            return
        cont = [0, 0, 0, 0]
        cars = {
            'road1': [],
            'road2': [],
            'road3': [],
            'road4': []
        }
        for car in system:
            if car.pos[3] == 'road1' and car.pos[1] < 175:
                cont[0] += 1
                cars['road1'].append(car)
            elif car.pos[3] == 'road2' and car.pos[1] > 235:
                cont[1] += 1
                cars['road2'].append(car)
            elif car.pos[3] == 'road3' and car.pos[0] < 140:
                cont[2] += 1
                cars['road3'].append(car)
            elif car.pos[3] == 'road4' and car.pos[0] > 200:
                cont[3] += 1
                cars['road4'].append(car)
        if cont == [0, 0, 0, 0]:
            return
        max = [cont[0],0]
        for i in range(4):
            if cont[i] > max[0]:
                max = [cont[i], i]
        if max[1] == 3:
            for value in cars['road4']:
                if value.pos[0] < 215:
                    value.your_turn = True
                    break
        if max[1] == 1:
            for value in cars['road2']:
                if value.pos[1] < 250:
                    value.your_turn = True
                    break
        if max[1] == 0:
            for value in cars['road1']:
                if value.pos[1] > 160:
                    value.your_turn = True
                    break
        if max[1] == 2:
            for value in cars['road3']:
                if value.pos[1] > 125:
                    value.your_turn = True
                    break


class Car:
    def __init__(self, name, pos, direction, vel, intentions, figure, size, turn, count, start_time, entry, exit):
        self.name = name
        self.pos = pos
        self.direction = direction
        self.vel = vel
        self.intentions = intentions
        self.figure = figure
        self.size = size
        self.turn = turn
        self.count = count
        self.start_time = start_time
        self.entry = entry
        self.exit = exit
        self.your_turn = False
        self.information = []
        self.give_up = False
    
    def detect_car(self, radius, cars):
        self.information = []
        for car in cars:
            distance = math.sqrt((car.pos[0] - self.pos[0])**2 + (car.pos[1] - self.pos[1])**2)
            if car.name != self.name and distance < radius:
                #print(car.name)
                self.information.append([car.name, car.pos, car.vel, car.direction])
    
    def make_decision_free_road(self):
        if self.give_up:
            return
        if is_out(self):
            #print('is out, ', self.pos[3], self.exit[1])
            return 'is out'
        if self.pos[3] == 'entry1' or self.pos[3] == 'entry2' or (self.pos[3] == 'return1' and self.pos[1] < 240) or (self.pos[3] == 'return2' and self.pos[1] > 170):
            self.make_entry()
            if self.vel == 0:
                return
        if self.pos[3] == 'return1':
            for value in self.information:
                if math.sqrt((value[1][0] - self.pos[0])**2 + (value[1][1] - self.pos[1])**2) < self.size[0] and value[1][3] == 'return1' and is_ahead(self.pos, value[1], self.direction, value[3]):
                    self.vel = 0
                    return     
            self.vel = 30
                
        if right_position(self):
            marc = 'do nothing'
            marc2 = 10000
            for value in self.information:
                if is_ahead(self.pos, value[1], self.direction, value[3]):
                    if marc2 > value[2] - self.vel:
                        marc2 = value[2] - self.vel
                        marc = 0
            if (marc == 'do nothing' and self.vel < speed_limit[self.pos[3]]):
                self.vel += 2 
            elif marc != 'do nothing':
                self.vel += marc2
        if self.intentions == [] and self.pos[3] != self.exit[1]:
            if self.pos[3] == 'road5':
                if self.exit[1] != 'out2':
                    self.intentions.append('road6')
                else:
                    self.intentions.append('out2')
            elif self.pos[3] == 'road6':
                if self.exit[1] == 'road5' or self.exit[1] == 'out2':
                    self.intentions.append('road5')
                else:
                    self.intentions.append('road7')
            elif self.pos[3] == 'road7':
                if self.exit[1] == 'road5' or self.exit[1] == 'out2' or self.exit[1] == 'road6':
                    self.intentions.append('road6')
                elif self.exit[1] == 'road4' or self.exit[1] == 'road2' or self.exit[1] == 'road1':
                    self.intentions.append('road4')
                else:
                    self.intentions.append('road8')
            elif self.pos[3] == 'road8':
                if self.exit[1] == 'road9' or self.exit[1] == 'out1' or self.exit[1] == 'road10':
                    self.intentions.append('road9')
                else:
                    self.intentions.append('road7')
            elif self.pos[3] == 'road9':
                if self.exit[1] != 'road10' and self.exit[1] != 'out1':
                    self.intentions.append('road8')
                else:
                    self.intentions.append('road10')
            elif self.pos[3]=='road10':
                if self.exit[1] != 'out1':
                    self.intentions.append('road9')
                else:
                    self.intentions.append('out1')
        else:
            marc = True  
            for value in self.information:
                if self.intentions!=[]:
                    if check_side(self.intentions[0], value[1][3], self.pos[0], value[1][0], self.size[0]):
                        marc = False
                        break
            if marc:

                return 'change lane'
            marc = 'do nothing'
            marc2 = 10000
            for value in self.information:
                if is_ahead(self.pos, value[1], self.direction, value[3]):
                    if marc2 > value[2] - self.vel:
                        marc2 = value[2] - self.vel
                        marc = 0
            if (marc == 'do nothing' and self.vel < speed_limit[self.pos[3]]):
                self.vel += 2 
            elif marc != 'do nothing':
                self.vel += marc2

    def make_decision_cross(self):
        if self.vel > 30:
            self.vel = 30
        if is_out(self):
            return 'is out'
        marc = 'do nothing'
        marc2 = 10000
        for value in self.information:
            if is_ahead(self.pos, value[1], self.direction, value[3]):
                if self.pos[3] == 'road4' or self.pos[3] == 'road3':
                    if (self.pos[0] - value[1][0])**2 < 2*((self.size[0])**2):
                        if marc2 > value[2] - self.vel:
                            marc2 = value[2] - self.vel
                            marc = 0
                elif self.pos[3] == 'road1' or self.pos[3] == 'road2':
                    if (self.pos[1] - value[1][1])**2 < 2*((self.size[0])**2):
                        if marc2 > value[2] - self.vel:
                            marc2 = value[2] - self.vel
                            marc = 0
        
        if self.pos[3] == 'road4' and self.pos[0] < 215 and self.your_turn == False:
            self.vel = 0
            return
        elif self.pos[3] == 'road3' and self.pos[0] > 125 and self.your_turn == False:
            self.vel = 0
            return
        elif self.pos[3] == 'road2' and self.pos[1] < 250 and self.your_turn == False:
            self.vel = 0
            return
        elif self.pos[3] == 'road1' and self.pos[1] > 160 and self.your_turn == False:
            self.vel = 0
            return
        elif (marc == 'do nothing' and self.vel < speed_limit[self.pos[3]]):
            self.vel = 30 
        if marc != 'do nothing':
            self.vel += marc2
        if self.intentions == [] and self.pos[3] != self.exit[1]:
            if self.pos[3] == 'road2':
                if self.exit[1] == 'road4':
                    self.intentions.append('road4')
                else:
                    self.intentions.append('road3')
            if self.pos[3] == 'road1':
                if self.exit[1] == 'road4':
                    self.intentions.append('road4')
                else:
                    self.intentions.append('road3')
            if self.pos[3] == 'road3':
                if self.exit[1] == 'road1':
                    self.intentions.append('road1')
                elif self.exit[1] == 'road2':
                    self.intentions.append('road2')
                else:
                    self.intentions.append('road8')
            if self.pos[3] == 'road4':
                if self.exit[1] == 'road1':
                    self.intentions.append('road1')
                else:
                    self.intentions.append('road2')
                
            


        

    def make_entry(self):
        if self.pos[3] == 'entry1' and self.pos[0] <= 887 and self.pos[1] >= 60 and self.pos[1] <= 75:
            enter = True
            for value in self.information:
                if value[1][3] == 'road5' and value[1][0] + self.size[0] > self.pos[0]:
                    enter = False
            if not enter:
                self.vel = 0
            else:
                self.vel = 40
        elif self.pos[3] == 'return1' and self.pos[1] >= 220 and self.pos[1] <= 235:
            enter = True
            for value in self.information:
                if value[1][3] == 'road8' and value[1][0] - self.size[0] < self.pos[0]:
                    enter = False
            if not enter:
                self.vel = 0
            else:
                self.vel = 40
        elif self.pos[3] == 'return2' and self.pos[1] <= 195 and self.pos[1] >= 175:
            enter = True
            for value in self.information:
                if value[1][3] == 'road7' and value[1][0] + self.size[0] > self.pos[0]:
                    enter = False
            if not enter:
                self.vel = 0
            else:
                self.vel = 40
        if self.pos[3] == 'entry2' and self.pos[0] <= 544 and self.pos[1] <= 350 and self.pos[1] >= 335:
            enter = True
            for value in self.information:
                if value[1][3] == 'road10' and value[1][0] - self.size[0] < self.pos[0]:
                    enter = False
            if not enter:
                self.vel = 0
            else:
                self.vel = 40
        

                    
def is_out(car):
    if car.pos[3] in ['road5', 'road7', 'road6'] and car.pos[0] < -23:
        return True
    elif car.pos[3] in ['road8', 'road9', 'road10'] and car.pos[0] > 1148:
        return True
    elif car.pos[3] == 'out2' and car.pos[0] <= 260:
        return True
    elif car.pos[3] == 'out1' and car.pos[0] >= 939:
        return True
    elif car.pos[3] == 'road4' and car.pos[0] < -23:
        return True
    return False


def check_side(obj, car_pos, car_1, car_2, size):
    if obj == car_pos:
        #print (obj, car_pos, car_1, car_2, size)
        #if car_2 + 3*size < car_1 or car_2 - 3*size > car_1:
        if car_2 <= car_1 + size and car_2 >= car_1 - size:
            return True
    return False

def is_ahead(pos1, pos2, dir1, dir2):
    if pos1[3] == pos2[3]:
        if pos2[0] > pos1[0] and dir1[0] > 0 and dir2[0] > 0:
            return True
        elif pos2[0] < pos1[0] and dir1[0] < 0 and dir2[0] < 0:
            return True
        elif pos2[1] > pos1[1] and dir1[1] > 0 and dir2[1] > 0:
            return True
        elif pos2[1] < pos1[1] and dir1[1] < 0 and dir2[1] < 0:
            return True
    return False

def right_position(car):
    if car.pos[3] == car.exit[1]:
        return True
    elif car.pos[3]== 'road5' and car.exit[1] == 'out2':
        return True
    elif car.pos[3] == 'road7' and car.exit[1] != 'road6' and car.exit[1] != 'road5':
        return True
    elif car.pos[3] == 'road8' and car.exit[1] != 'road9' and car.exit[1] != 'road10':
        return True
    elif car.pos[3] == 'road10' and car.exit[1] == 'out1':
        return True
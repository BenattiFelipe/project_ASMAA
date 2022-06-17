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
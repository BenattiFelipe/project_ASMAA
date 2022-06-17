from django.db import connection
import numpy as np
from utils import pos_to_index
from cars import Car
from roads import Road
import re
import random
import static
from datetime import datetime

class Environment:
    def __init__(self,cars,roads,entries,exits,connection,crosses,grid=2):
        self.cars = cars
        self.crosses = crosses
        self.roads = roads
        self.entries = entries
        self.exits = exits
        self.connection = connection
        self.grid = grid
        self.time = 0
    
    def add_road(self,road,pos): # pos = (orientaton,(x,y))
        R = np.zeros((road.nlength,int(round(road.width/self.grid))))
        self.roads.update({road.name:(road,pos,R)})
    
    def add_exit(self, exit):
        road = self.roads[exit.road.name][0]
        R = self.roads[exit.road.name][-1]
        pos = self.roads[exit.road.name][1]
        i = exit.lane
        j = exit.pos
        R[i,j] = -1
        self.roads.update({road.name:(road,pos,R)})
        self.exits.update({exit.name:exit})

    def add_entry(self,entry):
        road = self.roads[entry.road.name][0]
        R = self.roads[entry.road.name][-1]
        pos = self.roads[entry.road.name][1]
        i = entry.lane
        j = entry.pos
        R[i,j] = 1
        self.roads.update({road.name:(road,pos,R)})
        self.entries.update({entry.name:entry})

    def add_connection(self,connection):
        self.connection.update({connection.name:connection})
    
    def add_cross(self,cross):
        self.crosses.update({cross.name:cross})

    def add_car(self,car):
        self.cars.update({car.name:car})

    def lines_full(self):
        for entry in self.entries.values():
            if len(entry.line) == 0:
                return False
        return True

    def entries_tax_to_array(self,prob_no=0.001):
        probabilities = []
        for entry_name in self.entries.keys():
            entry = self.entries[entry_name]
            if len(entry.line) == 0:
                probabilities.append(entry.tax)
            else:
                probabilities.append(0)
        probabilities.append(prob_no)
        return np.array(probabilities)

    def play_entries(self,car_num,car_size):
        prob = self.entries_tax_to_array()
        entries = list(self.entries.keys())
        exits = self.find_only_exit()
        ent = np.random.choice(np.arange(0,len(self.entries.keys())+1), p=prob/prob.sum())
        ext = np.random.choice(np.arange(0,len(exits)), p=np.ones(len(exits))/np.ones(len(exits)).sum())
        if ent != len(self.entries.keys()):
            car_name = 'car'+'_'+str(car_num)
            print("criado",car_name)
            entry = self.entries[entries[ent]]
            line = entry.line.copy()
            line.append(car_name)
            entry.line = line.copy()
            self.entries.update({entries[ent]:entry})
            car = Car(car_name,(entry,(entry.lane,entry.pos)),car_size,ext_goal=self.exits[exits[ext]])
            car.path = car.looping_find_path(self,ref = car.road.road,path = [])
            self.cars.update({car.name:car})
            return car_num+1
        print("não criado")
        return car_num
        
    def draw_roads(self):
        for road in self.roads.keys():
            r = self.roads[road][0]
            R = self.roads[road][2]
            string = ''
            for i in range(len(R)):
                for j in R[i]:
                    if j==0:
                        string += '_'
                    elif j==1:
                        string += 'x'
                    elif j==-1:
                        string += 'o'
                if r.ways[i] == 1:
                    string += "\n------>"
                else:
                    string += "\n<------"
                string += '\n'
            print(string)

    def dic_environment_cars(self):
        dic = {}
        for road in self.roads.keys():
            dic.update({road:[]})
        for carname in self.cars.keys():
            car = self.cars[carname]
            if car.road.name in self.entries.keys():
                dic[car.road.road.name].append(car)
            else:
                dic[car.road.name].append(car)
        return dic

    def draw_cars(self):
        dic = self.dic_environment_cars()
        for road in dic.keys():
            R = np.zeros_like(self.roads[road][2])
            for car in dic[road]:
                index = re.findall('[0-9]',car.name)
                string = ''
                for i in index:
                    string+=i
                # print(pos_to_index(car.pos,self.roads[road][0].width,self.grid))
                R[car.lane][int(pos_to_index(car.pos,self.roads[road][0].width,self.grid))] = int(string)
            for i in R :
                s = ''
                for j in i:
                    if j == 0:
                        s += '_'
                    else:
                        s += str(j)
                print(s)
            print('\n')
                
    def communication_cars(self,range_detection):
        dic = {}
        dic_road = self.dic_environment_cars()
        for road in dic_road.keys():
            for car in dic_road[road]:
                dic.update({car.name:[]})
                for car2 in dic_road[road]:
                    if car2.name != car.name:
                        if abs(car.pos - car2.pos) <= range_detection:
                            dic[car.name].append(car2.name)
        return dic

    def entries_and_exits(self):
        entries = {}
        exities = {}
        for road_name in self.roads.keys():
            entries.update({road_name:[]})
            exities.update({road_name:[]})
            for entry_name in self.entries.keys():
                if self.entries[entry_name].road.name == road_name:
                    entries[road_name].append(entry_name)
            for exit_name in self.exits.keys():
                if self.exits[exit_name].road.name == road_name:
                    exities[road_name].append(exit_name)
        return entries, exities
    
    def find_connections(self):
        dic = {}
        dic_exit = {}
        dic_entry ={}
        dic_path = {}
        for connection_name in self.connection.keys():
            connection = self.connection[connection_name]
            dic_exit.update({connection.ext.name:[]})
            dic_entry.update({connection.ent.name:[]})
            try:
                dic[(connection.ext.road.name,connection.ent.road.name)].append(connection.name)
            except KeyError:
                dic.update({(connection.ext.road.name,connection.ent.road.name):[]})
                dic[(connection.ext.road.name,connection.ent.road.name)].append(connection.name)
            dic_exit[connection.ext.name].append(connection.name)
            dic_entry[connection.ent.name].append(connection.name)
            dic_path.update({(connection.ext.name,connection.ent.name):(connection.name,0,0)})
        return dic, dic_path, dic_exit, dic_entry
            
    def find_only_entry(self):
        only = []
        _, _, _, dic_entry = self.find_connections()
        for entry in self.entries.keys():
            if entry not in dic_entry.keys():
                only.append(entry)
        return only
    
    def find_only_exit(self):
        only = []
        _, _, dic_exit, _ = self.find_connections()
        for exit in self.exits.keys():
            if exit not in dic_exit.keys():
                only.append(exit)
        return only

    def one_entry_all_exities(self,pos,road,lane,exities):
        possible_exities = []
        for exit_name in exities[road.name]:
            exit = self.exits[exit_name]
            side = road.ways[lane]
            if side*exit.pos < side*pos:
                possible_exities.append(exit_name)
        return possible_exities

    def pop_car(self,car_name):
        self.cars.pop(car_name)
    

# cars = []
# for i in range(100):
#     entry = static.entries[random.randint(0, 10)]
#     exit = static.exits[random.randint(0, 10)]
#     position = static.define_position(entry)
#     velocity = static.define_velocity(entry)
#     cars.append('car#' + str(i), position, velocity, 0, [24, 12], datetime.now, exit, 0, 0)

# roads = ['road5', 'road6', 'road7']



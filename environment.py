import numpy as np
from utils import pos_to_index
from cars import Car
import re


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
        road = self.roads[exit.pos[0].name][0]
        R = self.roads[exit.pos[0].name][-1]
        pos = self.roads[exit.pos[0].name][1]
        i = exit.pos[1][0]
        j = exit.pos[1][1]
        R[i,j] = -1
        self.roads.update({road.name:(road,pos,R)})
        self.exits.update({exit.name:exit})

    def add_entry(self,entry):
        road = self.roads[entry.pos[0].name][0]
        R = self.roads[entry.pos[0].name][-1]
        pos = self.roads[entry.pos[0].name][1]
        i = entry.pos[1][0]
        j = entry.pos[1][1]
        R[i,j] = 1
        self.roads.update({road.name:(road,pos,R)})
        self.entries.update({entry.name:entry})

    def add_connection(self,connection):
        self.connection.update({connection.name:connection})
    
    def add_cross(self,cross):
        self.crosses.update({cross.name:cross})

    def add_car(self,car):
        self.cars.update({car.name:car})

    def play_entries(self,t,car_num):
        size_car = self.grid
        for ent in self.entries.keys():
            entry = self.entries[ent]
            if entry.tax!=0 and t*entry.tax - t*entry.tax%1 == 0:
                car = Car('car'+'_'+str(car_num),(entry.pos[0],(entry.pos[1][0],entry.pos[1][1])),0,0,size_car)
                car_num += 1
                self.add_car(car)
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

    def dic_road_cars(self):
        dic = {}
        for road in self.roads.keys():
            dic.update({road:[]})
        for carname in self.cars.keys():
            car = self.cars[carname]
            dic[car.pos[0].name].append(car)
        return dic

    def draw_cars(self):
        dic = self.dic_road_cars()
        for road in dic.keys():
            R = np.zeros_like(self.roads[road][2])
            for car in dic[road]:
                index = re.findall('[0-9]',car.name)
                string = ''
                for i in index:
                    string+=i
                R[car.pos[1][0]][pos_to_index(car.pos[1][1],self.roads[road][0].width,self.grid)] = int(string)
            for i in R :
                s = ''
                for j in i:
                    if j == 0:
                        s += '_'
                    else:
                        s += str(j)
                print(s)
            print('\n')
                
    def detection_cars(self,range_detection):
        dic = {}
        dic_road = self.dic_road_cars()
        for road in dic_road.keys():
            for car in dic_road[road]:
                detected_cars = []
                for car2 in dic_road[road]:
                    if car2.name != car.name:
                        if abs(car.pos[1][1] - car2.pos[1][1]) <= range_detection:
                            detected_cars.append(car2.name)
                dic.update({car.name:detected_cars})
        return dic

    def delete_car(self,car_name):
        self.cars.pop(car_name)

        
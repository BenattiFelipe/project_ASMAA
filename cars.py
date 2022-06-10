import numpy as np

class Car:
    def __init__(self,name,pos,vel,accel,size,ext_goal=None,start_time=0,grid_accel=1,penalization=0):
        self.name = name
        self.pos = pos # (Road,(lane,pos))
        self.vel = vel
        self.accel = accel
        self.size = size
        self.start_time = start_time
        self.ext_goal = ext_goal
        self.grid_accel = grid_accel
        self.penalization = penalization
        self.reward = 0
        self.time = 0
        self.actions = ['speed_up','slow_down','move_lane_rigth','move_lane_left','take_exit']
        # self.actions = ['speed_up','slow_down','move_lane_rigth','move_lane_left','take_exit','make_entry','wait']
    
    
    def move_straigth(self, dt):
        self.vel += self.accel*dt
        self.pos = (self.pos[0],(self.pos[1][0],self.pos[1][1] + self.vel*dt)) #+ 0.5*self.accel*dt**2

    def recive_penalization(self):
        self.penalization =+ 1

    def communication_cars(self,dict_car):
        return dict_car[self.name]

    def knowledge(self,env):
        return (env.exities, env.connections)

    ### Actions ####
    def speed_up(self):
        self.accel =+ self.grid_accel
    
    def slow_down(self):
        self.accel =- self.grid_accel

    def move_lane_rigth(self):
        pos = self.pos[1][0]+np.sign(self.pos[0].ways[self.pos[1][0]])*1
        self.pos = (self.pos[0],(pos,self.pos[1][1]))

    def move_lane_left(self):
        pos = self.pos[1][0]+np.sign(self.pos[0].ways[self.pos[1][0]])*-1
        self.pos = (self.pos[0],(pos,self.pos[1][1]))

    def take_exit(self,exit,env):
        self.pos = exit.pos
        if exit == self.ext_goal:
            self.reward =+ 1
            env.delete_car(self.name)
    
    def make_entry(self,entry):
        self.entry = entry.pos

    def wait():
        pass
    ####################################

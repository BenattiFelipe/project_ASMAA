import numpy as np

class Car:
    def __init__(self,name,pos,size,ext_goal=None,start_time=0,grid_accel=1,penalization=0):
        self.name = name
        self.road = pos[0]
        self.lane = pos[1][0]
        self.pos = pos[1][1]
        self.vel = 0
        self.accel = 0
        self.size = size
        self.start_time = start_time
        self.ext_goal = ext_goal
        self.grid_accel = grid_accel
        self.penalization = penalization
        self.reward = 0
        self.time = 0
        self.messages = []
        self.actions = ['speed_up','slow_down','move_lane_rigth','move_lane_left','take_exit']
        self.path = []
        # self.actions = ['speed_up','slow_down','move_lane_rigth','move_lane_left','take_exit','make_entry','wait']
    
    
    def move(self, dt):
        self.vel = self.vel+ self.accel*dt
        self.pos = self.pos + np.sign(self.road.ways[self.lane])*self.vel*dt #+ 0.5*self.accel*dt**

    def recive_penalization(self):
        self.penalization =+ 1

    def knowledge_cars(self,dict_car):
        return dict_car[self.name]


    ### Actions ####
    def speed_up(self):
        self.accel =+ self.grid_accel
    
    def slow_down(self):
        self.accel =- self.grid_accel

    def move_lane_rigth(self):
        self.lane = self.lane+np.sign(self.road.ways[self.lane])*1
        
    def move_lane_left(self):
        self.lane = self.lane+np.sign(self.road.ways[self.lane])*-1


    def take_exit(self,exit,env):
        self.pos = exit.pos
        self.lane = exit.lane
        self.road = exit.road
        if exit == self.ext_goal:
            self.reward =+ 1
            env.delete_car(self.name)
    
    def make_entry(self,entry):
        self.pos = entry.pos
        self.lane = entry.lane
        self.road = entry.road

    def wait():
        pass

    def looping_find_path(self,env,ref,path,possible_exities=[]):
        dic_c, dic_p,dic_ex, _ = env.find_connections()
        _, exities = env.entries_and_exits()
        # print(self.name,self.ext_goal.name,self.ext_goal.road.name,ref.name,exities[ref.name])
        only_exities = env.find_only_exit()
        ext_connection = list(dic_ex.keys())
        if ref.name == self.ext_goal.road.name:
                path.append(self.ext_goal.name)
                return path
        else:
            for ext in ext_connection:
                if ext not in only_exities:
                    con = dic_ex[ext][0]
                    ent = env.connection[con].ent
                    if ent.road.name == self.ext_goal.road.name:
                        path.append(ext)
                        path.append(ent.name)
                        self.looping_find_path(env,ent.road,path)
        return path

    # def find_path_connection(self,env):                ###########cruzamento
    #     dic_c, dic_p,dic_ex, _ = env.find_connections()
    #     _, exities = env.entries_and_exits()

            

    def find_path(self,env):
        path = []
        new = []
        ref = self.road
        dic_c, dic_p, _, _ = env.find_connections()
        _, exities = env.entries_and_exits()
        if ref.name in env.entries.keys():
            ref = ref.road
        #     possible_exities = exities[ref.road.name]
        # else:
        possible_exities = exities[ref.name]
        for ext in possible_exities:
            if self.pos*ref.ways[self.lane] < env.exits[ext].pos*ref.ways[self.lane]:
                new.append(ext)
                if ext == self.ext_goal.name:
                    path.append(ext)
                    return path
        possible_exities = new
        if dic_c.get((ref.name,self.ext_goal.road.name),0):
            possible_exities = []
            new = []
            path.append(ext)
            con_name = dic_c[(ref.name,self.ext_goal.road.name)][0] ###### mais perto
            con = env.connection[con_name]
            ref = con.ent.road
            path.append(con.ent.name)
        if ref.name in env.entries.keys():
            ref = ref.road
        #     possible_exities = exities[ref.road.name]
        # else:
        possible_exities = exities[ref.name]
        for ext in possible_exities:
            if self.pos*ref.ways[self.lane] > env.exits[ext].pos*ref.ways[self.lane]:
                new.append(ext)
                if ext == self.ext_goal.name:
                    path.append(ext)
                    # print(1,self.name,path)
                    return path
        # print(2,self.name, path)
        return path




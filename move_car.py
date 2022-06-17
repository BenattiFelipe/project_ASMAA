from rules import detect_collision_lane_left
from rules import detect_collision_lane_rigth
from rules import detect_collision_straight, can_enter, nobody_in_front, should_take_exit, exit_pass
import numpy as np

def detect_collision_move(car,env,cars,grid,dt,possible_actions=["speed_up","slow_down","wait","move_lane_rigth","move_lane_left","take_exit","make_entry"]):
    if detect_collision_lane_rigth(car,env,cars) or car.lane == 0:
        if "move_lane_rigth" in possible_actions:
            possible_actions.remove("move_lane_rigth")
    if detect_collision_lane_left(car,env,cars) or car.lane == 2:
        if "move_lane_left" in possible_actions:
            possible_actions.remove("move_lane_left")
    return possible_actions

def find_actions(car,env,dt):
    possible_actions = ["speed_up","slow_down","vel_const","move_lane_rigth","move_lane_left","take_exit"]
    if car.road.name in env.entries.keys():
        return ["make_entry","wait"]
    else:
        possible_actions = detect_collision_move(car,env.cars,env,env.grid,dt,possible_actions)
        return possible_actions

def define_best_action(car,env,communication_cars,dt):
    possible_actions = find_actions(car,env,dt)
    knowledge = car.knowledge_cars(communication_cars)
    if possible_actions[0] == 'make_entry':
        if can_enter(car,env,knowledge):
            return "make_entry"
        else:
            return 'wait'
    else:
        if car.vel == car.road.speedlimit and "speed_up" in possible_actions:
            possible_actions.remove("speed_up")
        if len(car.path)>0:
            # if car.name == "car_0":
                # print("te",car.path[0] in env.exits.keys() ,car.pos == env.exits[car.path[0]].pos ,car.lane == env.exits[car.path[0]].lane)
                # print(car.lane, env.exits[car.path[0]].lane)
                # print("lane",car.path[0] in env.exits.keys() ,car.pos != env.exits[car.path[0]].pos ,car.lane > env.exits[car.path[0]].lane,"move_lane_left" in possible_actions)
                # print("lane_r",car.path[0] in env.exits.keys() ,car.pos != env.exits[car.path[0]].pos ,car.lane < env.exits[car.path[0]].lane,"move_lane_rigth" in possible_actions)
                # print(possible_actions)
                # print("su",car.path[0] in env.exits.keys(),car.pos != env.exits[car.path[0]].pos,car.lane == env.exits[car.path[0]].lane, "speed_up" in possible_actions)
            # print(car.name,"path",car.path)
            # print((-car.pos*np.sign(car.road.ways[car.lane]) + np.sign(car.road.ways[car.lane])*env.exits[car.path[0]].pos))
            
            # print(car.road.name,car.pos,env.exits[car.path[0]].pos)
            if should_take_exit(car,env,knowledge):    
                return "take_exit"
            if exit_pass(car,env,knowledge): ### Penalization
                if len(car.path)>1:
                    print(car.name,car.ext_goal.name,car.path)
                    car.path = car.path[2:]
                    car.pos = env.exits[car.path[-1]].pos
                return "take_exit"
            if car.path[0] in env.exits.keys() and car.pos != env.exits[car.path[0]].pos and car.lane < env.exits[car.path[0]].lane and "move_lane_left" in possible_actions:
                return "move_lane_left"
            if car.path[0] in env.exits.keys() and car.pos != env.exits[car.path[0]].pos and car.lane > env.exits[car.path[0]].lane and "move_lane_rigth" in possible_actions:
                return "move_lane_rigth"
            if nobody_in_front(car,env,knowledge) and "speed_up" in possible_actions:
                return "speed_up"
            if car.path[0] in env.exits.keys() and car.pos != env.exits[car.path[0]].pos and car.lane == env.exits[car.path[0]].lane and "speed_up" in possible_actions:
                return "speed_up"
            
            return "vel_const"

def move_car(car,path,env,action, acc, dcc, dt):
    finish = False
    # print("acc",action)
    dic = {"speed_up":1,"slow_down":2,"vel_const":3,"move_lane_rigth":4,"move_lane_left":5,"take_exit":6,"make_entry":7}
    if dic[action] == dic["speed_up"]:
        car.accel = acc
        car.move(dt)
    if dic[action] == dic["slow_down"]:
        car.accel = dcc
        car.move(dt)
    if dic[action] == dic["vel_const"]:
        car.accel = 0
        car.move(dt)
    if dic[action] == dic["move_lane_rigth"]:
        car.lane -= 1
        car.move(dt)
    if dic[action] == dic["move_lane_left"]:
        car.lane += 1
        car.move(dt)
    if dic[action] == dic["take_exit"]:
        if car.ext_goal.name == car.path[0]:
            finish = True
            car.path = []
        else:
            car.road = env.entries[car.path[1]]
            line = env.entries[car.path[1]].line.copy()
            line.append(car.name)
            env.entries[car.path[1]].line = line.copy()
            car.lane = env.entries[car.path[1]].lane
            car.pos = env.entries[car.path[1]].pos
            # print(path)
            rest_path = car.path[2:]
            car.path = rest_path.copy()
            # print("AA","path",path)
    if dic[action] == dic["make_entry"]:
        # print("EEEEEEEEEEEEEEEEE")
        env.entries[car.road.name].line = []
        car.vel = 0
        car.accel = acc
        car.pos = car.road.pos
        car.lane = car.road.lane
        car.road = car.road.road
        # print("BBBB",car.path)
        car.path = car.path.copy()
        car.move(dt)
    return finish
        

        
    
        
    



# def chose_best_action(car,cars,grid,dt,possible_actions):
#     if 
#         car.slow_down()
#         return "slow_down"
#     else:
#         return "speed_up"
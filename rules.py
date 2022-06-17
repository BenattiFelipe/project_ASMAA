# Penalization rules
# Crashs
# Speed fee

# Car Action
# - Straight
# - Speed up
# - Slow down
# - Lane rigth
# - Lane left
# - Wait
# - Take exit
# - Make entry

from sympy import symbols,solve
import numpy as np

def detect_collision_straight(car,cars,env):
    t = symbols('t',real = True)
    bol = True
    for k in cars:
        c = env.cars[k]
        if c.lane==car.lane:
            c_vel = c.vel
            c_pos = c.pos
            if car.vel <= c_vel:
                bol = False
            ts = solve(np.sign(car.road.ways[car.lane])*(car.pos+t*car.vel*t+t*car.accel*t**2 - c.pos+t*c.vel*t + t*c.accel*t**2),t)
            if len(ts)==0:
                return False
            for time in ts:
                if time>0 and c.road.width - c.pos*np.sign(car.road.ways[car.lane]) < np.sign(car.road.ways[car.lane])*(car.pos+time*car.vel*time+time*car.accel*time**2):
                    return True
    return False


def detect_collision_lane_rigth(car,cars,env):
    future_car = car
    future_car.lane = car.lane - 1
    pos1 = future_car.pos
    if len(cars) == 0 or car.lane == 0:
        return False
    for k in cars:
        c = env.cars[k]
        # if car.name == "car_1":
        #     print("R:",k,c.lane,future_car.lane,abs(c.pos-pos1),car.size/2)
        if c.lane==future_car.lane and abs(c.pos-pos1) <= car.size/2 and k!=car.name:
            return True
    return False

def detect_collision_lane_left(car,cars,env):
    future_car = car
    future_car.lane = car.lane + 1
    pos1 = future_car.pos
    if len(cars) == 0 or car.lane == car.road.nlength-1:
        return False
    for k in cars:
        c = env.cars[k]
        # print("A:",k,c.lane,future_car.lane,abs(c.pos-pos1),car.size/2)
        if c.lane==future_car.lane and abs(c.pos-pos1) <= car.size/2 and k!=car.name:
            return True
    return False

def can_enter(car,env,knowledge):
    if len(knowledge) == 0:
        return True
    else:
        can = True
        for k in knowledge:
            c = env.cars[k]
            if c.lane != car.lane and can == True:
                 can = True
            elif can == True:
                c_vel = c.vel
                c_pos = c.pos
                if car.accel > 0:
                    t_acc = abs(car.vel - c_vel)/car.accel
                    t_col = abs((car.pos+t_acc*car.accel*t_acc**2) - c_pos )/c_vel
                    if t_col < t_acc:
                        can = False
        return can

def nobody_in_front(car,env,knowledge):
    t = symbols('t',real = True)
    bol = True
    c_more_close = ""
    for k in knowledge:
        c = env.cars[k]
        if c.lane==car.lane and c.name!=car.name:
            c_vel = c.vel
            c_pos = c.pos
            if car.pos*np.sign(car.road.ways[car.lane]) <= c_pos*np.sign(car.road.ways[car.lane]):
                bol = False
                if "" == c_more_close:
                    c_more_close = c.name
                else:
                    if abs(car.pos-c_pos) < abs(car.pos-env.cars[c_more_close].pos):
                        c_more_close = c.name
    if bol == False:
        c = env.cars[c_more_close]
        ts = solve(np.sign(car.road.ways[car.lane])*(car.pos+t*car.vel*t+t*car.accel*t**2 - c.pos+t*c.vel*t + t*c.accel*t**2),t)
        if len(ts)==0:
            for time in ts:
                if time>0 and c.road.width - c.pos*np.sign(car.road.ways[car.lane]) < np.sign(car.road.ways[car.lane])*(car.pos+time*car.vel*time+time*car.accel*time**2):
                    bol = True
    return bol

def should_take_exit(car,env,knowledge):

    if car.path[0] in list(env.exits.keys()) and car.lane == env.exits[car.path[0]].lane:
        ext = env.exits[car.path[0]]
        sig = np.sign(car.road.ways[car.lane])
        pos_exit = sig*ext.pos
        if (-car.pos*sig + sig*pos_exit)<=0:
            return True
    return False

def exit_pass(car,env,knowledge):
    if car.path[0] in list(env.exits.keys()) and car.lane != env.exits[car.path[0]].lane:
        ext = env.exits[car.path[0]]
        sig = np.sign(car.road.ways[car.lane])
        pos_exit = sig*ext.pos
        if (-car.pos*sig + sig*pos_exit)<=0:
            return True
    return False
# if detect_collision_straight(car,cars,grid,dt):
# if "move_straigth" in possible_actions:
#     possible_actions.remove("move_straigth")
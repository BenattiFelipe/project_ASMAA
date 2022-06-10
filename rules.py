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

from turtle import pos

def detect_collision_straight(car,cars,grid,dt):
    future_car = car
    future_car.move_straigth(dt)
    pos1 = future_car.pos[1][1]
    for c in cars:
        if c.pos[1]==future_car.pos[1]:
            if abs(pos1 - c.pos[1][1]) <= grid/2:
                return True
    return False


def detect_collision_lane_rigth(car,cars,grid,dt):
    future_car = car
    future_car.move_lane_rigth()
    pos1 = future_car.pos[1][1]
    for c in cars:
        if c.pos[1][0]==future_car.pos[1][0] and abs(c.pos[1][1]-pos1) <= grid/2:
            return True
    return False

def detect_collision_lane_left(car,cars,grid,dt):
    future_car = car
    future_car.move_lane_left()
    pos1 = future_car.pos[1][1]
    for c in cars:
        if c.pos[1][0]==future_car.pos[1][0] and abs(c.pos[1][1]-pos1) <= grid/2:
            return True
    return False

def detect_colision_move(car,cars,grid,dt,possible_actions=["speed_up","slow_down","wait","move_lane_rigth","move_lane_left","take_exit","make_entry"]):
    if detect_collision_lane_rigth(car,cars,grid,dt):
        if "move_lane_rigth" in possible_actions:
            possible_actions.remove("move_lane_rigth")
    if detect_collision_lane_left(car,cars,grid,dt):
        if "move_lane_left" in possible_actions:
            possible_actions.remove("move_lane_left")
    return possible_actions


# if detect_collision_straight(car,cars,grid,dt):
# if "move_straigth" in possible_actions:
#     possible_actions.remove("move_straigth")
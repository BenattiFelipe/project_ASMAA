import numpy as np
from utils import pos_to_index
from cars import Car
from roads import Road, Entry, Exit, Connection, Cross
from environment import Environment
from move_car import define_best_action
import rules
import move_car


grid = 1

env = Environment({},{},{},{},{},{},grid)

# R1 = Road("R1",2,60,[1,-1],30)
# en11 = Entry("en11",(R1,(0,0)),0.5,env.grid)  # Pos = (pos,faixa)
# en12 = Entry("en12",(R1,(1,60)),0.5,env.grid) 
# ex11 = Exit("ex11",1,(R1,(0,60)),30,env.grid)
# ex12 = Exit("ex12",1,(R1,(1,0)),30,env.grid)

# R2 = Road("R2",2,48,[1,-1],30)
# en21 = Entry("en21",(R2,(0,0)),0.5,env.grid)
# en22 = Entry("en22",(R2,(1,48)),0.5,env.grid)
# ex21 = Exit("ex21",1,(R2,(0,48)),30,env.grid)
# ex22 = Exit("ex22",1,(R2,(1,0)),30,env.grid)

# cr12 = Cross("cr12",(R1,R2),(22,32))

R3 = Road("R3",3,140,[-1,-1,-1],50)
ex31 = Exit("ex31",1,(R3,(0,0)),50,env.grid)
ex32 = Exit("ex32",1,(R3,(1,0)),50,env.grid)
ex33 = Exit("ex33",1,(R3,(2,0)),50,env.grid)
ex34 = Exit("ex34",1,(R3,(0,120)),50,env.grid)
en31 = Entry("en31",(R3,(0,140)),0.5,env.grid)
en32 = Entry("en32",(R3,(1,140)),0.5,env.grid)
en33 = Entry("en33",(R3,(2,140)),0.5,env.grid)
en34 = Entry("en34",(R3,(0,100)),0.5,env.grid)

en_con1 = Entry("en_con1",(R3,(0,75)),0,env.grid)
ex_con1 = Exit("ex_con1",1,(R3,(0,85)),50,env.grid)

R4 = Road("R4",3,140,[1,1,1],50)
ex41 = Exit("ex41",1,(R4,(0,140)),50,env.grid)
ex42 = Exit("ex42",1,(R4,(1,140)),50,env.grid)
ex43 = Exit("ex43",1,(R4,(2,140)),50,env.grid)
ex44 = Exit("ex44",1,(R4,(2,40)),50,env.grid)
en41 = Entry("en41",(R4,(0,0)),0.5,env.grid)
en42 = Entry("en42",(R4,(1,0)),0.5,env.grid)
en43 = Entry("en43",(R4,(2,0)),0.5,env.grid)
en44 = Entry("en44",(R4,(2,10)),0.5,env.grid)

en_con2 = Entry("en_con2",(R4,(0,85)),0,env.grid)
ex_con2 = Exit("ex_con2",1,(R4,(0,75)),50,env.grid)

con1 = Connection("con1",en_con1,ex_con2,2)
con2 = Connection("con2",en_con2, ex_con1,2)

# ent = [en11,en12,en21,en22,en31,en32,en33,en34,en41,en42,en43,en44]
# ex = [ex11,ex12,ex21,ex22,ex31,ex32,ex33,ex34,ex41,ex42,ex43,ex44]
# env.add_road(R1,(0,(0,0))) # pos = (orientaton,(x,y))
# env.add_road(R2,(1,(0,0))) # Orientatio 0 = horizontal, 1 = vertical
env.add_road(R3,(0,(0,0)))
env.add_road(R4,(0,(0,0)))

ent = [en31,en32,en33,en34,en41,en42,en43,en44,en_con1,en_con2]
ex = [ex31,ex32,ex33,ex34,ex41,ex42,ex43,ex44,ex_con1,ex_con2]
con = [con1,con2]

for e in ent:
    env.add_entry(e)
for e in ex:
    env.add_exit(e)
for e in con:
    env.add_connection(e)

env.draw_roads()

acc = 0.5
dacc = 0.5

# env.interaction(10)
np.random.seed(40)
# for i in range(10):
#     env.play_entries(len(env.cars),env.grid)
# for car in env.cars:
#     print(env.cars[car].name,env.cars[car].pos,define_best_action(env.cars[car],env,env.communication_cars(15)))
# car10 = Car('car03',(R3,(20,50)),10,1,2,ext_goal=ex34)
# env.add_car(car10)
car_num = len(env.cars)
for t in range(100):
    i = 0.5*t
    print()
    print(f"---------------------------{i}---------------------------")
    # env.draw_cars()
    print()
    if i%2 == 0 :
        car_num = env.play_entries(car_num,env.grid)
    list_finish = []
    # for ent_name in env.entries:
    #     ent = env.entries[ent_name]
    #     print(ent.name,ent.pos,ent.line)
    for car in env.cars.keys():
        k = env.cars[car]
        # print(car,"pos",k.pos,"lane",k.lane,"ac",k.accel,"k.vel",k.vel,k.road.name,k.path,(k.ext_goal.road.name,k.ext_goal.lane))
        if len(env.cars[car].path)>0:
            action = move_car.define_best_action(env.cars[car],env,env.communication_cars(15),1)
            finish = move_car.move_car(env.cars[car],env.cars[car].path,env, action, acc, dacc, 1)
            if finish:
                list_finish.append(car)
        else:
            list_finish.append(car)
        # print(car,"pos",k.pos,"lane",k.lane,"ac",k.accel,"k.vel",k.vel,k.road.name,k.path,(k.ext_goal.road.name,k.ext_goal.lane),action)
    for car in list_finish:
        env.pop_car(car)
    print()
    if env.lines_full():
        print("lines full")
    try:
        print(len(env.cars),car_num)
        env.draw_cars()
    except:
        pass
    print("-------------------------------------------------------------------")
# car1 = Car('car01',(R4,(0,0)),10,4,2, entry = en41 ,ext_goal=ex32)
# car2 = Car('car02',(R3,(1,45)),10,1,2, entry = en32 , ext_goal=ex42)
# env.add_car(car1)
# env.add_car(car2)
# env.add_car(car3)

# # print(env.detection_cars(10))

# env.draw_cars()

# car1.move_straigth(1)
# car2.move_straigth(1)
# car3.move_straigth(1)
# env.add_car(car1)
# env.add_car(car2)
# env.add_car(car3)

# env.draw_cars()

# car1.move_straigth(1)
# car2.move_straigth(1)
# car3.move_straigth(1)
# car3.move_lane_left()
# env.add_car(car1)
# env.add_car(car2)
# env.add_car(car3)

# dic = env.dic_road_cars()

# pm = move_car.detect_collision_move(car2,dic[car2.road.name],env.grid,1)
# print(pm)

# env.draw_cars()

# #32,34,47,48,92,
# #51,152,157

# for car in env.cars.values():
#     print(car.name,car.lane,car.pos,car.vel,car.accel)


# print("P",car1.find_path(env))
# print(ex41.pos,ex41.lane,ex41.road)
import random
#Static
global turn1, turn2, turn3, turn4, turn5, turn6, turn7, turn8, turn9, turn10, turn11, turn12, turn13, turn14, turn15, turn16, turn17, turn18, turn19, turn20, turn21, turn22, count
turn1 = ['turn1', 218, 90] # down to right
turn2 = ['road4', 190, -90] # down to left
turn3 = ['road3', 218, 90] # up to right
turn4 = ['road4', 190, 270] # up to left
turn5 = ['r', 155, 0] # left to down 
turn6 = ['turn6', 185, 180] # left to up 
turn7 = ['road1', 155, 0]
turn8 = ['road2', 185, 180]
turn9 = [['road8', 406, 0], ['road8', 255, 90]]
turn10 = ['roa9']
turn11 = ['road10']
turn12 = ['road9']
turn13 = ['road8']
turn14 = [['road7', 785, 180], ['road7', 155, -90]]
turn15 = ['roa6']
turn16 = ['road5']
turn17 = ['road6']
turn18 = ['road7']
turn19 = [['road8', 640, 180], ['road8', 255, -90]]
turn20 = [['road4', 406, 0], ['road4', 190, 90]]
turn21 = [['road5', 887, 0], ['road5', 95, -90]]
turn22 = [['road10', 530, 180], ['road10', 315, -90]]
turn23 = [['out1', 899, 180], ['out1', 346, -90]]
turn24 = [['out2', 300, 180], ['out2', 64, -90]]


entry1 = [156, -23, 0, 0, 1, 'road1']
entry2 = [184, 401, 180, 0, -1, 'road2']
entry3 = [-23, 219, 90, 1, 0, 'road3']
entry4 = [-23, 256, 90, 1, 0, 'road8']
entry5 = [-23, 284, 90, 1, 0, 'road9']
entry6 = [-23, 313, 90, 1, 0, 'road10']
entry7 = [1148, 124 , -90, -1, 0, 'road6']
entry8 = [1148, 96 , -90, -1, 0, 'road5']
entry9 = [1148, 154 , -90, -1, 0, 'road7']
entry10 = [930, 55, -90, -1, 0, 'entry1']
entry11 = [490, 355, 90, 1, 0, 'entry2']

exit1 = [-23, 'road5', '']
exit2 = [-23, 'road6', '']
exit3 = [-23, 'road7', '']
exit4 = [1048, 'road8', '']
exit5 = [1048, 'road9', '']
exit6 = [1048, 'road10', '']
exit7 = [401, 'road1', '']
exit8 = [-23, 'road2', '']
exit9 = [-23, 'road4', '']
exit10 = [0, 'out1', 'road10']
exit11 = [0, 'out2', 'road5']

#entries = entries = [entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11]
entries = [entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11]
#exits = [exit1, exit2, exit3, exit4, exit5, exit6, exit9, exit10, exit11]
exits = [exit1, exit2, exit3, exit4, exit5, exit6, exit7, exit8, exit9, exit10, exit11]

def define_position(entry):
    return ([entry[0], entry[1], entry[2], entry[5]])

def define_velocity(entry):
    #return [0.1*random.randint(5, 10)*entry[3], 0.1*random.randint(5, 10)*entry[4]]
    return [entry[3], entry[4]]

def define_exit(entry):
    random_number = random.randint(1, 100)
    if entry == entry1:
        if random_number <= 25:
            exits = [exit7]
        elif random_number <= 40:
            exits = [exit9]
        elif random_number <= 90:
            exits = [exit1, exit2, exit3, exit4, exit5, exit6]
        else:
            exits = [exit8, exit10, exit11]
    elif entry == entry2:
        if random_number <= 25:
            exits = [exit8]
        elif random_number <= 40:
            exits = [exit9]
        elif random_number <= 90:
            exits = [exit1, exit2, exit3, exit4, exit5, exit6]
        else:
            exits = [exit7, exit10, exit11]
    elif entry == entry3 :
        if random_number <= 20:
            exits = [exit7]
        elif random_number <= 40:
            exits = [exit9]
        elif random_number <= 90:
            exits = [exit1, exit2, exit3, exit4, exit5, exit6]
        else:
            exits = [exit9, exit10, exit11]
    elif entry == entry4 or entry == entry5 or entry == entry6 or entry == entry10:
        if random_number <= 70:
            exits = [exit4, exit5, exit6]
        elif random_number <= 90:
            exits = [exit1, exit2, exit3]
        elif random_number <= 95:
            exits = [exit11]
        else:
            exits = [exit7, exit8, exit9, exit10]
    elif entry == entry7 or entry == entry8 or entry == entry9 or entry == entry11:
        if random_number <= 70:
            exits = [exit1, exit2, exit3]
        elif random_number <= 90:
            exits = [exit4, exit5, exit6]
        elif random_number <= 95:
            exits = [exit10]
        else:
            exits = [exit7, exit8, exit9, exit11]
    return exits[random.randint(0, len(exits)-1)]
    

def define_entry(entries):
    new_entry = []
    for i in range (30):
        new_entry.append(entries[3])
        new_entry.append(entries[4])
        new_entry.append(entries[5])
        new_entry.append(entries[6])
        new_entry.append(entries[7])
        new_entry.append(entries[8])
    for i in range(30):
        new_entry.append(entries[0])
        new_entry.append(entries[1])
        new_entry.append(entries[2])
    for i in range (5):
        new_entry.append(entries[9])
        new_entry.append(entries[10])
    return new_entry[random.randint(0, 279)]

speed_limit = {
    'road1': 30,
    'road2': 30,
    'road3': 30,
    'road4': 30,
    'road5': 50,
    'road6': 50,
    'road7': 50,
    'road8': 50,
    'road9': 50,
    'road10': 50,
    'entry1': 50,
    'entry2': 50,
    'out1':50,
    'out2': 50,
    'return1': 50,
    'return2':50
}
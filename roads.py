from utils import pos_to_index

class Road:
    def __init__(self,name,nlength,width,ways,speedlimit):
        length = 2
        self.name = name
        self.nlength = nlength
        self.length = nlength*length
        self.width = width
        self.ways = ways
        self.speedlimit = speedlimit

class Connection():
    def __init__(self,name,ent,ext,num_car):
        self.name = name
        self.ent = ent
        self.ext = ext
        self.num_car = num_car


class Entry():
    def __init__(self,name,pos,tax,grid):
        self.name = name
        self.pos = (pos[0],(pos[1][0],pos_to_index(pos[1][1],pos[0].width,grid)))
        self.tax = tax
    
    def effective_tax(self,tax):
        self.tax = tax

class Exit():
    def __init__(self,name,nlength,pos,speedlimit,grid):
        self.name = name
        self.nlength = nlength
        self.pos = (pos[0],(pos[1][0],pos_to_index(pos[1][1],pos[0].width,grid)))  # pos = (Road, pos=(way,posx))
        self.speedlimit = speedlimit

class Cross():
    def __init__(self,name,roads,pos):
        self.roads = roads
        self.name = name
        self.pos = pos

    def get_exities_entries_connections(self,env):
        ent_cross_00 = Entry(self.name+'_'+"entry_00",(self.roads[0],(0,self.pos[0])),0,env.grid)
        ent_cross_01 = Entry(self.name+'_'+"entry_01",(self.roads[0],(-1,self.pos[0])),0,env.grid)
        ent_cross_10 = Entry(self.name+'_'+"entry_10",(self.roads[1],(0,self.pos[1])),0,env.grid)
        ent_cross_11 = Entry(self.name+'_'+"entry_11",(self.roads[1],(-1,self.pos[1])),0,env.grid)
        ext_cross_00 = Exit(self.name+'_'+"exit_00",self.roads[1].nlength,(self.roads[0],(0,self.pos[0])),self.roads[1].speedlimit,env.grid)
        ext_cross_01 = Exit(self.name+'_'+"exit_01",self.roads[1].nlength,(self.roads[0],(-1,self.pos[0])),self.roads[1].speedlimit,env.grid)
        ext_cross_10 = Exit(self.name+'_'+"exit_10",self.roads[0].nlength,(self.roads[1],(0,self.pos[1])),self.roads[0].speedlimit,env.grid)
        ext_cross_11 = Exit(self.name+'_'+"exit_11",self.roads[0].nlength,(self.roads[1],(-1,self.pos[1])),self.roads[0].speedlimit,env.grid)

        con_cross_00 = Connection(self.name+'_'+"connection_00",ent_cross_00,ext_cross_00,1)
        con_cross_01 = Connection(self.name+'_'+"connection_01",ent_cross_01,ext_cross_01,1)
        con_cross_10 = Connection(self.name+'_'+"connection_10",ent_cross_10,ext_cross_10,1)
        con_cross_11 = Connection(self.name+'_'+"connection_11",ent_cross_11,ext_cross_11,1)

        return([ent_cross_00,ent_cross_01,ent_cross_10,ent_cross_11],[ext_cross_00,ext_cross_01,ext_cross_10,ext_cross_11],[con_cross_00,con_cross_01,con_cross_10,con_cross_11])



import matplotlib.pyplot as plt
from static import *


def plot(analyses, time_factor, colision_location):    
    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return '{p:.1f}%  ({v:d})'.format(p=pct,v=val)
        return my_autopct
    labels = 'Reached', 'Unreached', 'Crashed'
    sizes = [len(analyses['reached objective']), len(analyses['unreached objective']), len(analyses['crashed'])]

    colors = ['#00876c','#4c9c85','#78b19f','#a0c6b9', '#c8dbd5','#f1f1f1','#f1cfce','#eeadad','#e88b8d','#df676e','#d43d51']
    
    pie = plt.pie(sizes, startangle=0, autopct=make_autopct(sizes), pctdistance=0.9, radius=1.2)
    plt.title('General Overview', weight='bold', size=14)

    plt.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, 
            bbox_transform=plt.gcf().transFigure)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.85)

    plt.savefig('Results/general overview')
    plt.show()



    free_roads_in = [entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11]
    crosses_in = [entry1, entry2, entry3]
    free_roads_out = [exit1, exit2, exit3, exit4, exit5, exit6, exit10, exit11]
    crosses_out = [exit7, exit8, exit9]

    aux0 = [0,0,0,0,0,0,0,0,0,0,0]
    aux1 = [0,0,0,0,0,0,0,0,0,0,0]
    aux2 = [0,0,0,0,0,0,0,0,0,0,0]
    aux3 = [[0,0,0] for i in range(11)]
    for i in range(11):
        for car in analyses['reached objective']:
            if car.entry == entries[i]:
                aux1[i] += 1
                aux3[i][0] += 1
        for car in analyses['unreached objective']:
            if car.entry == entries[i]:
                aux2[i] += 1
                aux3[i][1] += 1
        for car in analyses['crashed']:
            if car.entry == entries[i]:
                aux0[i] += 1
                aux3[i][2] += 1
    free_road_to_free_road = [0,0,0]
    free_road_to_cross = [0,0,0]
    cross_to_free_road = [0,0,0]
    cross_to_cross = [0,0,0]
    time_bank = [0,0,0]
    time_bank_2 = [0,0,0,0]
    factor = [0,0,0,0]

    for car in analyses['reached objective']:
        time_bank[0] += car.time*time_factor
        if car.entry in free_roads_in and car.exit in free_roads_out:
            free_road_to_free_road[0] += 1
            time_bank_2[0] += car.time*time_factor
            factor[0] += 1
        if car.entry in free_roads_in and car.exit in crosses_out:
            free_road_to_cross[0] += 1
            time_bank_2[1] += car.time*time_factor
            factor[1] += 1
        if car.entry in crosses_in and car.exit in free_roads_out:
            cross_to_free_road[0] += 1
            time_bank_2[2] += car.time*time_factor
            factor[2] += 1
        if car.entry in crosses_in and car.exit in crosses_out:
            cross_to_cross[0] += 1
            time_bank_2[3] += car.time*time_factor
            factor[3] += 1
    for car in analyses['unreached objective']:
        time_bank[1] += car.time*time_factor
        if car.entry in free_roads_in and car.exit in free_roads_out:
            free_road_to_free_road[1] += 1
            time_bank_2[0] += car.time*time_factor
            factor[0] += 1
        if car.entry in free_roads_in and car.exit in crosses_out:
            free_road_to_cross[1] += 1
            time_bank_2[1] += car.time*time_factor
            factor[1] += 1
        if car.entry in crosses_in and car.exit in free_roads_out:
            cross_to_free_road[1] += 1
            time_bank_2[2] += car.time*time_factor
            factor[2] += 1
        if car.entry in crosses_in and car.exit in crosses_out:
            cross_to_cross[1] += 1
            time_bank_2[3] += car.time*time_factor
            factor[3] += 1
    for car in analyses['crashed']:
        time_bank[2] += car.time*time_factor
        if car.entry in free_roads_in and car.exit in free_roads_out:
            free_road_to_free_road[2] += 1
            time_bank_2[0] += car.time*time_factor
            factor[0] += 1
        if car.entry in free_roads_in and car.exit in crosses_out:
            free_road_to_cross[2] += 1
            time_bank_2[1] += car.time*time_factor
            factor[1] += 1
        if car.entry in crosses_in and car.exit in free_roads_out:
            cross_to_free_road[2] += 1
            time_bank_2[2] += car.time*time_factor
            factor[2] += 1
        if car.entry in crosses_in and car.exit in crosses_out:
            cross_to_cross[2] += 1
            time_bank_2[3] += car.time*time_factor
            factor[3] += 1

    print('average time:')
    print((time_bank[0] + time_bank[1] + time_bank[2])/(len(analyses['reached objective'])+len(analyses['unreached objective']) + len(analyses['crashed'])))
    time_bank[0] = time_bank[0]/len(analyses['reached objective'])
    time_bank[1] = time_bank[1]/len(analyses['unreached objective'])
    time_bank[2] = time_bank[2]/len(analyses['crashed'])
    time_bank_2[0] = time_bank_2[0]/factor[0]
    time_bank_2[1] = time_bank_2[1]/factor[1]
    time_bank_2[2] = time_bank_2[2]/factor[2]
    time_bank_2[3] = time_bank_2[3]/factor[3]

    data = {'Free road to free road':time_bank_2[0], 'Free road to cross':time_bank_2[1], 'Cross to free road':time_bank_2[2], 'Cross to cross': time_bank_2[3]}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values,
            width = 0.4)
    
    plt.xlabel("Startpoints and endpoints")
    plt.ylabel("Average Time")
    plt.title("Average time considering goals")
    plt.savefig('Results/average_time_goals')
    plt.show()



    titles = ['Free road to free road', 'Free road to cross', 'Cross to free road', 'Cross to cross']
    plots = [free_road_to_free_road, free_road_to_cross, cross_to_free_road, cross_to_cross]
    for i in range (4):
        sizes = plots[i]
        
        pie = plt.pie(sizes, startangle=0, autopct=make_autopct(sizes), pctdistance=0.9, radius=1.2)
        plt.title(titles[i], weight='bold', size=14)
        plt.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, 
            bbox_transform=plt.gcf().transFigure)
        plt.subplots_adjust(left=0.0, bottom=0.1, right=0.85)
        plt.savefig('Results/'+titles[i])
        plt.show()

    data = {'Reached goal':time_bank[0], 'Do not reached goal':time_bank[1], 'Crashed':time_bank[2]}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values,
            width = 0.4)
    
    plt.xlabel("Results")
    plt.ylabel("Average Time")
    plt.title("Average time and Results")
    plt.savefig('Results/average time')
    plt.show()

    colision_map = [0, 0]
    for value in colision_location:
        if value in ['road1', 'road2', 'road3', 'road4']:
            colision_map[0] += 1
        else:
            colision_map[1] += 1

    sizes = colision_map
        
    pie = plt.pie(sizes, startangle=0, autopct=make_autopct(sizes), pctdistance=0.9, radius=1.2)
    plt.title('Overview of the colisions', weight='bold', size=14)
    plt.legend(pie[0],['Crosses', 'Free roads'], bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, 
        bbox_transform=plt.gcf().transFigure)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.85)

    plt.savefig('Results/colisions overview')
    plt.show()

    labels2 = ['entry' + str(i) for i in range(1, 12)]
    aux = [aux0, aux1, aux2]
    ocurences = ['Crash', 'Reach Objective', 'Do not Reach Objective']
    for i in range(3):
        sizes = aux[i]
        
        pie = plt.pie(sizes, startangle=0, autopct=make_autopct(sizes), pctdistance=0.9, radius=1.2, colors=colors)
        plt.title(ocurences[i], weight='bold', size=14)
        plt.legend(pie[0],labels2, bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, 
            bbox_transform=plt.gcf().transFigure)
        plt.subplots_adjust(left=0.0, bottom=0.1, right=0.85)
        plt.savefig('Results/'+ocurences[i])
        plt.show()

    for i in range(11):
        sizes = aux3[i]

        pie = plt.pie(sizes, startangle=0, autopct=make_autopct(sizes), pctdistance=0.9, radius=1.2)
        plt.title('Entry' + str(i + 1), weight='bold', size=14)
        plt.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, 
            bbox_transform=plt.gcf().transFigure)
        plt.subplots_adjust(left=0.0, bottom=0.1, right=0.85)
        plt.savefig('Results/entry'+str(i+1))
        plt.show()

    print(len(analyses['surpassed speed limit']))
import random
import math
from time import sleep
beach_size = [100,100]
org_list = {}


class Org():
    def __init__(self, name, age, is_alive, life, repro_min, repro_interval, repro_baby_no, tank, energy, menu, pos, move_range, angle, forwardp, is_close_to, near_food):
        self.name = name
        self.age = age
        self.is_alive = is_alive
        # Life and reproduction
        self.life = life
        self.repro_min = repro_min
        self.repro_interval = repro_interval
        self. repro_baby_no = repro_baby_no
        # Food
        self.tank = tank
        self.energy = energy
        self.menu = menu
        # Movement and location
        self.pos = pos
        self.move_range = move_range
        self.angle = angle

        self.forwardp = forwardp
        self.sidep = 100 - forwardp
        # Relations
        self.is_close_to = is_close_to
        self.near_food = near_food

    def move(self):
        rand_num = random.randint(1,100)
        # if rand_num > self.forwardp:
        
        if self.name != "plant":
            if self.pos[1] == 100 and (self.pos[0] != 1 or self.pos[0] != 100):
                self.angle = 3
            elif self.pos[1] == 1 and (self.pos[0] != 1 or self.pos[0] != 100):
                self.angle = 1
            
            elif self.pos[0] == 100 and (self.pos[1] != 1 or self.pos[1] != 100):
                self.angle = 4

            elif self.pos[0] == 1 and (self.pos[1] != 1 or self.pos[1] != 100):
                self.angle = 2
            
            elif rand_num > self.forwardp:
                if random.randint(1,2) == 1:
                    if self.angle == 4:
                        self.angle = 1
                    else:
                        self.angle += 1
                else:
                    if self.angle == 1:
                        self.angle = 4
                    else:
                        self.angle -= 1
            
            move_dist = self.move_range[random.randint(self.move_range[0], self.move_range[1])]
            if self.angle == 1:
                self.pos[1] += move_dist
            elif self.angle == 2:
                self.pos[0] += move_dist
            elif self.angle == 3:
                self.pos[1] -= move_dist
            elif self.angle == 4:
                self.pos[0] -= move_dist


    def print_location(self):
        print(self.name, self.pos[0], self.pos[1])

    def kill(self):
        print("tried")
        self.is_alive = False
        self.pos = [0,0]


def get_proximities():
    for organism1 in org_list:
        for organism2 in org_list:
            if abs(org_list[organism1].pos[0] - org_list[organism2].pos[0]) <= 0 and abs(org_list[organism1].pos[1] - org_list[organism2].pos[1]) <= 0 and organism1 != organism2:
                if organism2 not in org_list[organism1].is_close_to:
                    org_list[organism1].is_close_to.append(organism2)
    for animals in org_list:
        print(animals)
        print(org_list[animals].is_close_to)

def move_animals():
    for animal in org_list:
        org_list[animal].move()

def kill_if_close():
    for animal in org_list:
        print(animal)
        if org_list[animal].name == "hamster" and len(org_list[animal].is_close_to) > 0 and org_list[org_list[animal].is_close_to[0]].name == "plant":
            for animals in org_list[animal].is_close_to:
                org_list[animals].kill()
        org_list[animal].is_close_to = []

def reproduce():
    for animal in org_list:
        if org_list[animal].age >= org_list[animal].repro_min:
            if org_list[animal].name == "plant":
                adjx = [org_list[animal].pos[0]-1, org_list[animal].pos[0], org_list[animal].pos[0]+1]
                adjy = [org_list[animal].pos[1]-1, org_list[animal].pos[1], org_list[animal].pos[1]+1]
                xy = []
                xy.append(adjx[random.randint(0,2)])
                xy.append(adjy[random.randint(0,2)])
                while xy == [org_list[animal].pos[0], org_list[animal].pos[1]]:
                    xy = []
                    xy.append(adjx[random.randint(0,2)])
                    xy.append(adjy[random.randint(0,2)])


# org_list[1] = Org("plant", 0, True, 200, 30, 5, [2,3], 0, 1.5, [], [50,60], [0,0], 1, 0, [])
for i in range(1,20):
    org_list[i] = Org("plant", 0, True, 200, 30, 5, [2,3], 0, 1.5, [], [50,30+i], [0,0], 1, 0, [], [])
for i in range(21,50):
    org_list[i] = Org("hamster", 0, True, 200, 30, 5, [2,3], 0, 1.5, [], [3+i,3], [0,0], 1, 70, [], [])
pop_counter = 10

def map():
    map = {}
    for i in range(1,101):
        map[i] = []
        map[i].append("|")
        for n in range(1,101):
            map[i].append(" ")
        map[i].append("|")
    for animals in org_list:
        if org_list[animals].is_alive:
            print(True)
            map[org_list[animals].pos[1]][org_list[animals].pos[0]-1] = org_list[animals].name.title()[0]

    

    print("_"*100)
    for i in reversed(range(1,101)):
        name = ""
        for chars in map[i]:
            name += chars
        print(name)
        name = ""
    print("_"*100 + "|")








while True:
    move_animals()
    get_proximities()
    kill_if_close()

    for animal in org_list:
        print(animal, org_list[animal].pos[0], org_list[animal].pos[1])


    
    map()
    sleep(0.1)
import random
from time import sleep

height = 5
width = 5
a = {}

# Create box
box = {}
for i in range(1,height+1):
    box[i] = [" "]*width



class Animal():
    def __init__(self, type, age, isAlive, canMove, pos, angle, hunger):
        self.type = type
        self.age = age
        self.isAlive = isAlive
        self.canMove = canMove
        self.pos = pos
        self.angle = angle
        self.hunger = hunger

        edit_box(self.pos[0], self.pos[1], self.type.upper()[0])

    def increase_age(self):
        self.age += 1

    def move(self):
        if self.canMove and self.isAlive:
            edit_box(self.pos[0], self.pos[1], " ")
            
            if self.angle == "up":
                self.pos[0] -= 1
            elif self.angle == "down":
                self.pos[0] += 1
            elif self.angle == "right":
                self.pos[1] += 1
            elif self.angle == "left":
                self.pos[1] -= 1
            
            edit_box(self.pos[0], self.pos[1], self.type.upper()[0])

    def turn(self, lor):
        if self.canMove and self.isAlive:
            if lor == "right":
                if self.angle == "up":
                    self.angle = "right"
                elif self.angle == "right":
                    self.angle = "down"
                elif self.angle == "down":
                    self.angle = "left"
                elif self.angle == "left":
                    self.angle = "up"
            elif lor == "left":
                if self.angle == "up":
                    self.angle = "left"
                elif self.angle == "left":
                    self.angle = "down"
                elif self.angle == "down":
                    self.angle = "right"
                elif self.angle == "right":
                    self.angle = "up"

    def kill(self):
        self.isAlive = False
        edit_box(self.pos[0], self.pos[1], " ")


# Write box
def write_box():
    print()
    for k,v in box.items():
        print(k, end=" ")
        print(v)

# Changes 1 character of box
def edit_box(r, c, char):
    if len(char) == 1:
        box[r][c-1] = char

# Checks if box is occupied
def is_occupied(r,c):
    if box[r][c-1] != " ":
        return True
    else:
        return False

def getNearBlocks(pos, dist):
    nearBlocksList = []
    for i in range(pos[0]-dist, pos[0]+dist+1):
        if i <= height and i >= 1:
            for n in range(pos[1]-dist, pos[1]+dist+1):
                if n <= width and n >= 1:
                    if not is_occupied(i,n):
                        nearBlocksList.append([i,n])
                    
    return nearBlocksList


def reproduce():
    counter = 0
    temp = []
    for anim in a:
        if a[anim].isAlive:
            temp.append(anim)
        counter = anim + 1

    spawn_blocks = []

    for anim in temp:
        if len(getNearBlocks(a[anim].pos, 1)) > 0:
            for block in random.sample(getNearBlocks(a[anim].pos, 1), min(3, len(getNearBlocks(a[anim].pos, 1)))):
                if block not in spawn_blocks:
                    spawn_blocks.append(block)
    
    for block in spawn_blocks:
        a[counter] = Animal(type="plant",
            age=0,
            isAlive=True,
            canMove=False,
            pos=block,
            angle="up",
            hunger=0)
        counter += 1


        
def checkAndKill():
    num = random.randint(10,15)
    
    for anim in a:
        if len(getNearBlocks(a[anim].pos, 1)) == 0 and a[anim].hunger < num:
            a[anim].hunger += 1
    
    
    kill_list = []
    for anim in a:
        if len(getNearBlocks(a[anim].pos, 1)) == 0 and a[anim].hunger == num:
            kill_list.append(anim)

    for anim in kill_list:
        a[anim].kill()
        del a[anim]


def day():
    sleep(0.1)
    checkAndKill()
    write_box()
    sleep(0.1)

    reproduce()

    write_box()




a[1] = Animal(type="plant",
            age=0,
            isAlive=True,
            canMove=False,
            pos=[25,25],
            angle="up",
            hunger=0)

a[2] = Animal(type="plant",
            age=0,
            isAlive=True,
            canMove=False,
            pos=[50,79],
            angle="up",
            hunger=0)


a[3] = Animal(type="hamster",
    age=0,
    isAlive=True,
    canMove=True,
    pos=[1,1],
    angle="up",
    hunger=0)


while True:
    day()
    # count = 0
    # for anim in a:
    #     count = anim
    # print(count)

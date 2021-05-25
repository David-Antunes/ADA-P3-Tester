from random import random,randint


tests = 1

chars = ['G','O','W']
def getRandom():
    prob = random()
    if prob < 0.15:
        return 1
    elif prob >= 0.15 and prob < 0.40:
        return 2
    else:
        return 0
print(tests)
for i in range(tests):
    rows = randint(3,15)
    cols = randint(3,15)
    wheels = randint(0,10)
    num_endings = 0
    num_wheels = 1

    print(str(rows) + " " + str(cols) + " " + str(wheels))

    world_map = []
    for row in range(rows):
        world_map.append([])

    for row in range(rows):
        for col in range(cols):
            if(row != 0 and col != 0 and row != rows - 1 and col != cols -1):    
                letter = chars[getRandom()]
            else:
                letter = 'W'
            # if letter == 'T' and num_wheels <= 9:
            #     letter = str(num_wheels)
            #     num_wheels += 1
            # else:
            #     while(letter == 'T'):
            #         letter = chars[getRandom()]
            world_map[row].append(letter)

    while(num_wheels < wheels):
        posX = randint(0, rows-1)
        posY = randint(0, cols-1)
        if(world_map[posX][posY] == 'G'):
            world_map[posX][posY] = str(num_wheels)
            num_wheels += 1

    while(num_endings == 0):
        posX = randint(0, rows-1)
        posY = randint(0, cols-1)
        if(world_map[posX][posY] == 'G'):
            world_map[posX][posY] = 'X'
            num_endings += 1

    for row in range(rows):
        line = ''
        for letter in world_map[row]:
            line += letter
        print(line)

    num_wheels = 0
    while(num_wheels < wheels):
        posX = randint(0, rows-1)
        posY = randint(0, cols-1)
        weight = randint(-100000, 100000)
        num_wheels += 1
        print( str(posX) + " " + str(posY) + " " + str(weight))

    num_persons = 0
    while(num_persons < 2):
        posX1 = randint(0, rows-1)
        posY1 = randint(0, cols-1)
        posX2 = randint(0, rows-1)
        posY2 = randint(0, cols-1)
        if(world_map[posX1][posY1] == 'G' and world_map[posX2][posY2] == 'G' and posX1 != posX2 and posY1 != posY2):
            print(str(posX1) + " " + str(posY1) + " " + str(posX2) + " " + str(posY2))  
            num_persons += 2
    


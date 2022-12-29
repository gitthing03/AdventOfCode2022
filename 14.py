def main():
    cave = makeCave()
    # Identify the deepest rock point
    deepest = -1
    for rockPile in cave:
        for rockY in cave[rockPile]:
            if rockY > deepest: deepest = rockY
    # Part 1
    sandCount = 0
    while True:
        if dropSand(cave, deepest): sandCount += 1
        else: break
    print("Part1: " + str(sandCount))
    # Part 2
    cave = makeCave()
    sandCount = 0
    while True:
        sandCount+=1
        if dropSandWithFloor(cave,deepest+2): break # deepest point for part 2 is part 1 + 2
    print("Part2: " + str(sandCount))

def dropSand(cave,d):
    x = 500
    y = 0
    while True:
        if (x not in cave or y+1 not in cave[x]) and y < d: y += 1
        elif (x-1 not in cave or y+1 not in cave[x-1]) and y < d:
            y += 1
            x -= 1
        elif (x+1 not in cave or y+1 not in cave[x+1]) and y < d:
            x += 1
            y += 1
        elif atRest(cave,x,y):
            cave[x].add(y)
            return True
        else: return False

def dropSandWithFloor(cave,floor):
    x = 500
    y = 0
    while True:
        # Add floor points to the left and right
        for v in [x, x-1, x+1]:
            if v not in cave:
                cave[v] = {floor}
            else:
                cave[v].add(floor)
        if y+1 not in cave[x] and y < floor:
             y += 1
        elif y+1 not in cave[x-1] and y < floor:
            y += 1
            x -= 1
        elif y+1 not in cave[x+1] and y < floor:
            x += 1
            y += 1
        elif atRest(cave,x,y) or y == floor-1:
            cave[x].add(y)
            if x == 500 and y == 0:
                return True
            return False
        else: return False
    
def atRest(cave,x,y): 
    if x not in cave or x-1 not in cave or x+1 not in cave: return False
    if y+1 in cave[x] and y+1 in cave[x-1] and y+1 in cave[x+1]: return True
    return False

# Reads input and initalizes a dictionary where keys are sets
# Each key is an x value, any value in a set represents rock being present at y (x,y)
def makeCave():
    cave = {}
    with open("inputs/14.txt", "r") as file:
        for line in [line.strip() for line in file.readlines()]:
            moves = line.split()
            prev = moves[0].split(",")
            prevX = int(prev[0])
            prevY = int(prev[1])
            for i in range(2,len(moves),2):
                cur = moves[i].split(",")
                curX = int(cur[0])
                curY = int(cur[1])
                if curX != prevX: # Horizontal rock
                    if curX > prevX: r = range(prevX, curX+1)
                    else: r = range(curX, prevX+1)
                    for j in r:
                        if j in cave: cave[j].add(curY)
                        else: cave[j] = {curY}
                else: # Vertical rock
                    if curY > prevY: r = range(prevY, curY+1)
                    else: r = range(curY, prevY+1)
                    for j in r:
                        if curX in cave: cave[curX].add(j)
                        else: cave[curX] = {j}
                prevX = curX
                prevY = curY
    return cave

if __name__ == "__main__":
    main()
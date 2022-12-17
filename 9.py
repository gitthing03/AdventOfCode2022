def main():
    print("Part1: " + tailPointsCount(2))
    print("Part2: " + tailPointsCount(10))

class Knot():
    def __init__(self, origin, parent=None):
        self.point = origin
        self.history = {tuple(origin)}
        self.parent = parent
        self.child = None
    def update(self):
        # If there is a space between point and parent, set space orientation flag
        moveHor = abs(self.parent.point[0]-self.point[0]) == 2
        moveVer = abs(self.parent.point[1]-self.point[1]) == 2
        # If not on same row and column, and not touching, move diagonally
        if not sameRow(self.parent.point, self.point) and not sameCol(self.parent.point, self.point) and not touching(self.parent.point, self.point):
            moveHor = True
            moveVer = True
        if moveHor:
            self.point[0] += 1 if self.parent.point[0] > self.point[0] else -1
        if moveVer:
            self.point[1] += 1 if self.parent.point[1] > self.point[1] else -1
        # Add point to knot history, and update child knot
        self.history.add(tuple(self.point))
        if self.child:
            self.child.update()

def tailPointsCount(knotCount):
    # Create knot chain of desired len
    head = Knot([0,0])
    prev = head
    for i in range(knotCount-1):
        new = Knot([0,0],prev)
        prev.child = new
        prev = new
    tail = new

    with open("inputs/9.txt", "r") as file:
        # For each movement
        for move in [line.strip().split() for line in file.readlines()]:
            dir = move[0]
            amt = int(move[1])
            # Go one step at a time
            for i in range(amt):
                if dir == "L":
                    head.point[0] -= 1
                elif dir == "R":
                    head.point[0] += 1
                elif dir == "U":
                    head.point[1] += 1
                else:
                    head.point[1] -= 1
                # Update all children accordingly
                head.child.update()
    return str(len(tail.history))

# If two points are within a point of eachother on both axes, they are touching
def touching(point1, point2):
    return (abs(point1[0]-point2[0]) < 2 and abs(point1[1]-point2[1]) < 2)

def sameRow(point1, point2):
    return point1[0] == point2[0]

def sameCol(point1, point2):
    return point1[1] == point2[1]

if __name__ == "__main__":
    main()
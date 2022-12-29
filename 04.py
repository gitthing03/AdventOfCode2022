def main():
    print("Part1: " + part1())
    print("Part2: " + part2())

def part1():
    with open("inputs/04.txt", "r") as file:
        numContains = 0
        for pair in file.readlines():
            # split string into two assignments
            splitAssignments = pair.split(",")
            # store each assignment
            assignment1 = splitAssignments[0]
            assignment2 = splitAssignments[1]
            # split each assignment by the "-", cast each var to int in a list
            assignment1Range = [int(x) for x in str(assignment1).split("-")]
            assignment2Range = [int(x) for x in str(assignment2).split("-")]
            # if the end points of one range fall within the endpoints of another, increment
            if assignment1Range[0] >= assignment2Range[0] and assignment1Range[1] <= assignment2Range[1]:
                numContains += 1
            elif assignment2Range[0] >= assignment1Range[0] and assignment2Range[1] <= assignment1Range[1]:
                numContains += 1
    return str(numContains)

def part2():
    with open("inputs/04.txt", "r") as file:
        numOverlaps = 0
        for pair in file.readlines():
        # split string into two assignments
            splitAssignments = pair.split(",")
            # store each assignment
            assignment1 = splitAssignments[0]
            assignment2 = splitAssignments[1]
            # split each assignment by the "-", cast each var to int in a list
            assignment1Range = [int(x) for x in str(assignment1).split("-")]
            assignment2Range = [int(x) for x in str(assignment2).split("-")]

            if assignment1Range[1] >= assignment2Range[0] and assignment1Range[0] <= assignment2Range[1]:
                numOverlaps += 1
            elif assignment2Range[1] >= assignment1Range[0] and assignment2Range[0] <= assignment1Range[1]:
                numOverlaps += 1

    return str(numOverlaps)

if __name__ == "__main__":
    main()

        

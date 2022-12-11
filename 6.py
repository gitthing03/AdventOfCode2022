def main():
    print("Part1: " + part1())
    print("Part2: " + part2())

def part1():
    # open input
    with open("inputs/6.txt", "r") as file:
        # read line
        for line in file.readlines():
            # starting at forth character, loop through every char
            for i in range(3, len(line)):
                # create a set
                chars = set()
                # add the current character and the last three characters to set
                for x in range(4):
                    chars.add(line[i-x])
                # if the len of set is 4, all unique
                if len(chars) == 4:
                    # return the index of the last char + 1 to indicate when a marker appeared
                    return str(i+1)

def part2():
    # open input
    with open("inputs/6.txt", "r") as file:
        # read line
        for line in file.readlines():
            # starting at fourteenth character, loop through every char
            for i in range(13, len(line)):
                # create a set
                chars = set()
                # add the current character and the last thirteen characters to set
                for x in range(14):
                    chars.add(line[i-x])

                # if the len of set is 14, all unique
                if len(chars) == 14:
                    # return the index of the last char + 1 to indicate when a message appeared
                    return str(i+1)

if __name__ == "__main__":
    main()
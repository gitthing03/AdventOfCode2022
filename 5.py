def main():
    print("Part1: " + part1())
    print("Part2: " + part2())

def part1():
    # grab cargo data
    cargo = nCargo()

    # open input
    with open("inputs/5.txt", 'r') as file:
        # read through commands
        for command in file.readlines():
            # split command string into seperate words
            words = command.split(" ")
            # second word is amount
            amt = int(words[1])
            # fourth word is origin
            frm = int(words[3])
            # sixth word is destination
            to = int(words[5])

            # for the amt
            for i in range(amt):
                # pop from the origin, and append to destination
                cargo[to].append(cargo[frm].pop())
        # string of top letters
        top = ""
        # for each stack
        for stack in cargo:
            # append the last letter (top) in the stack
            top += cargo[stack][-1]
    
    return top

def part2():
    # grab cargo data
    cargo = nCargo()
    
    # open input
    with open("inputs/5.txt", 'r') as file:
        # read commands
        for command in file.readlines():
            # split words in command
            words = command.split(" ")
            # amount is second word
            amt = int(words[1])
            # origin is fourth word
            frm = int(words[3])
            # destination is sixth word
            to = int(words[5])

            # create a list of creates being moved
            moving = []
            # starting from the lowest crate being moved, append all creates being moved to list
            for i in range(len(cargo[frm])-amt, len(cargo[frm])):
                moving.append(cargo[frm][i])

            # pop the number of crates being moved from origin
            for i in range(amt):
                cargo[frm].pop()
            
            # append each crate being moved to destination
            for crate in moving:
                cargo[to].append(crate)
        # string of top letters
        top = ""
        # for each stack
        for stack in cargo:
            # append the last letter (top) of the stack
            top += cargo[stack][-1]
    return top

def nCargo():
    # returns the original cargo data originally present in input data
    return {
        1: ['S', 'C', 'V', 'N'],
        2: ['Z', 'M', 'J', 'H', 'N', 'S'],
        3: ['M', 'C', 'T', 'G', 'J', 'N', 'D'],
        4: ['T', 'D', 'F', 'J', 'W', 'R', 'M'],
        5: ['P', 'F', 'H'],
        6: ['C', 'T', 'Z', 'H', 'J'],
        7: ['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z'],
        8: ['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W'],
        9: ['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z']
    }


if __name__ == "__main__":
    main()

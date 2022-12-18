def main():
    cycles = {1: 1}
    x = 1
    with open("inputs/10.txt", "r") as file:
        lines = [line.rstrip().split() for line in file.readlines()]
        i = 2
        inCycle = False
        # For each command
        for cmd in lines:
            # Create a loop
            while True:
                # If the command is noop, do nothing, go to next cycle, break loop
                if cmd[0] == "noop":
                    cycles[i] = x
                    i += 1
                    break
                # addx command
                else:
                    # if already ran the first part, add the new value, go to next cycle, and break
                    if inCycle:
                        x += int(cmd[1])
                        inCycle = False
                        cycles[i] = x
                        i += 1
                        break
                    # first part of addx, do nothing, increase cycle, go back to loop
                    else:
                        inCycle = True
                        cycles[i] = x
                        i += 1
    # Cycle numbers to add up values for
    ints = [20,60,100,140,180,220]
    total = 0
    for x in ints:
        total += x * cycles[x]
    print("Part1: " + str(total))

    # Print cycles 1-240 on six lines, put a '#' if the cycle value is +-1 of the current line index
    output = []
    cycle = 1
    for x in range(6):
        row = []
        for i in range(40):
            spriteMiddle = cycles[cycle]
            if i in range(spriteMiddle-1,spriteMiddle+2):
                row.append("#")
            else:
                row.append(".")
            cycle += 1
        output.append(row)
    # prints letters to screen
    print("Part2: ZFBFHGUP")
    for line in output:
        print(line)
    
if __name__ == "__main__":
    main()
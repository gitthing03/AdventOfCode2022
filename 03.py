def main():
    print("Part 1: " + part1())
    print("Part 2: " + part2())

def part1():
    # open file
    with open("inputs/3.txt", "r") as file:
        # set sum var
        sumPrio = 0
        # read lines
        for sack in file.readlines():
            # comparment 1 is first half of the string
            comp1 = sack[:len(sack)//2]
            # compartment 2 is the latter half of the string
            comp2 = sack[len(sack)//2:]
            # convert each comparment into a set
            cSet1 = set(comp1)
            cSet2 = set(comp2)
            # find intersections
            common = cSet1.intersection(cSet2)
            # for each intersection in the sack, add the value of the letter to the sum
            for letter in common:
                sumPrio += calcPrio(letter)
    return str(sumPrio)

def part2():
    # open file
    with open("inputs/3.txt", "r") as file:
        # set prio var
        sumPrio = 0
        # read lines
        f = file.readlines()
        # loop through lines in groups of 3
        for i in range(0, len(f), 3):
            # find the common letter in each 3 lines, remove \n
            common = set(f[i].rstrip()) & set(f[i+1].rstrip()) & set(f[i+2].rstrip())
            # add the value of the common letter to sum
            for letter in common:
                sumPrio += calcPrio(letter)
    return str(sumPrio)

# calculate the "priority" of a letter
def calcPrio(letter):
    # get ASCII value of letter
    letter = ord(letter)
    # if the value is < 91 (letter is uppercase)
    if letter < 91:
        # A-Z correspond to 27-52, substracting 65 from the ASCII value and adding 27 will get score
        return (letter-65)+27
    # letter is lowercase
    else:
        # a-z correspond to 1-26, subtracting 97 from the ASCII value and adding one will get score
        return (letter-97)+1 


if __name__ == "__main__":
    main()
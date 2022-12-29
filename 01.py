with open('inputs/01.txt', 'r') as file:
    currentCount = 0
    highestCount1 = 0
    highestCount2 = 0
    highestCount3 = 0
    for amt in file.read().split("\n"):
        if amt == "":
            if currentCount > highestCount3:
                if currentCount > highestCount2:
                    if currentCount > highestCount1:
                        highestCount3 = highestCount2
                        highestCount2 = highestCount1
                        highestCount1 = currentCount
                    else:
                        highestCount3 = highestCount2
                        highestCount2 = currentCount
                else:
                    highestCount3 = currentCount
            currentCount = 0
        else:
            currentCount += int(amt)

print("Part1: " + str(highestCount1))
print("Part2: " + str(highestCount1+highestCount2+highestCount3))

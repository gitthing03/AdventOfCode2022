def main():
    output = solution()
    print("Part1: " + output[0])
    print("Part2: " + output[1])

def solution():
    with open("inputs/8.txt", "r") as file:
        # create matrix of input
        lines = [line.rstrip() for line in file.readlines()]
        data = [[] for line in lines]
        for i in range(len(lines)):
            for char in range(len(lines[i])):
                data[i].append(int(lines[i][char]))

        # Every character will be no less than 0
        DEFAULT_CHAR_MAX = -1
        # Track amt of visible trees
        visibleCount = 0

        totalDistanceScore = 0

        for currentRowIndex in range(len(data)):
            currentRow = data[currentRowIndex]
            for currentColIndex in range(len(currentRow)):
                
                visibleCounted = False

                currentVal = currentRow[currentColIndex]
                
                leftStopped = False
                leftViewingDistance = currentColIndex
                # Find visibility and scenic val from the left
                leftMax = DEFAULT_CHAR_MAX
                if currentColIndex > 0:
                    for leftCharIndex in range(currentColIndex-1, -1, -1):
                        leftMax = max(currentRow[leftCharIndex], leftMax)
                        if not leftStopped and currentVal <= currentRow[leftCharIndex]:
                            leftViewingDistance = currentColIndex-leftCharIndex
                            leftStopped = True
                if leftMax < currentVal and not visibleCounted:
                    visibleCount += 1
                    visibleCounted = True
                
                rightStopped = False
                rightViewingDistance = len(currentRow)-currentColIndex-1
                # Find visibility and scenic val from the right
                rightMax = DEFAULT_CHAR_MAX
                if currentColIndex < len(currentRow)-1:
                    for rightCharIndex in range(currentColIndex+1, len(currentRow)):
                        rightMax = max(currentRow[rightCharIndex], rightMax)
                        if not rightStopped and currentRow[rightCharIndex] >= currentVal:
                            rightViewingDistance = rightCharIndex-currentColIndex
                            rightStopped = True
                if rightMax < currentVal and not visibleCounted:
                    visibleCount += 1
                    visibleCounted = True

                upStopped = False
                upViewingDistance = currentRowIndex
                # Find visibility and scenic val from the top
                upMax = DEFAULT_CHAR_MAX
                if currentRowIndex > 0:
                    for uRow in range(currentRowIndex-1, -1, -1):
                        upMax = max(data[uRow][currentColIndex], upMax)
                        if not upStopped and data[uRow][currentColIndex] >= currentVal:
                            upStopped = True
                            upViewingDistance = currentRowIndex-uRow
                if upMax < currentVal and not visibleCounted:
                    visibleCount += 1
                    visibleCounted = True

                downStopped = False
                downViewingDistance = len(data)-currentRowIndex-1
                # Find visibility and scenic val from the bottom
                downMax = DEFAULT_CHAR_MAX
                if currentRowIndex < len(data)-1:
                    for dRow in range(currentRowIndex+1, len(data)):
                        downMax = max(data[dRow][currentColIndex], downMax)
                        if not downStopped and data[dRow][currentColIndex] >= currentVal:
                            downStopped = True
                            downViewingDistance = dRow-currentRowIndex
                if downMax < currentVal and not visibleCounted:
                    visibleCount += 1
                    visibleCounted = True

                # Only consider a distance score if it is larger than the previous
                if totalDistanceScore < rightViewingDistance * downViewingDistance * leftViewingDistance * upViewingDistance:
                    totalDistanceScore = rightViewingDistance * downViewingDistance * leftViewingDistance * upViewingDistance

        # Output
        return (str(visibleCount)), str(totalDistanceScore)

if __name__ == "__main__":
    main()
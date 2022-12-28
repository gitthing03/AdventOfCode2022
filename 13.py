from ast import literal_eval

def main():
    packets = []
    # Parse input
    with open("inputs/13.txt", "r") as file:
        currentPair = []
        for line in [line.strip() for line in file.readlines()]:
            if len(currentPair) == 2:
                packets.append(currentPair)
                currentPair = []
            else:
                currentPair.append(literal_eval(line))
        packets.append(currentPair)
    
    allPackets = [[[2]], [[6]]]

    # Part 1
    rights = 0
    for i in range(len(packets)):
        compare = comparePackets(packets[i])
        allPackets.append(packets[i][0]) # Append each packet to list for part 2
        allPackets.append(packets[i][1])
        if compare: rights += i+1
    print("Part1: " + str(rights))

    # Part 2
    mergeSort(allPackets)
    decoder = i = 1
    for packet in allPackets:
        if packet == [[2]] or packet == [[6]]:
            decoder *= i
        i += 1
    print("Part2: " + str(decoder))

def comparePackets(packet):
    pair1 = packet[0]
    pair2 = packet[1]
    # Use the longer pair's length
    length = len(pair1) if len(pair1) > len(pair2) else len(pair2)
    for i in range(length): # Loop through pairs
        # If left ran out, true, if right ran out, false
        if i+1>len(pair1): return True
        elif i+1>len(pair2): return False
        # Otherwise
        if type(pair1[i]) is int and type(pair2[i]) is int:         # If both of the current vals are ints, compare
            compare = compareInts((pair1[i], pair2[i]))
        elif type(pair1[i]) is list and type(pair2[i]) is list:     # If both of the current vals are lists, compare the lists
            compare = compareLists((pair1[i], pair2[i]))
        else:                                                       # Different types
            if type(pair1[i]) is int:                               # Convert whichever value is an int to a list, then compare lists
                compare = compareLists(([pair1[i]], pair2[i]))
            else:
                compare = compareLists((pair1[i], [pair2[i]]))
        if compare != None: return compare

def compareLists(lists):
    # Use the longer list's length
    length = len(lists[0]) if len(lists[0]) > len(lists[1]) else len(lists[1])
    for i in range(length):
        # If left ran out, true, if right ran out, false
        if i+1>len(lists[0]):
            return True
        elif i+1>len(lists[1]):
            return False
        if type(lists[0][i]) is int and type(lists[1][i]) is int:           # If both of the current vals are ints, compare
            compare = compareInts((lists[0][i], lists[1][i]))
        elif type(lists[0][i]) is list and type(lists[1][i]) is list:       # If both of the current vals are lists, compare the lists
            compare = compareLists((lists[0][i], lists[1][i]))
        else:                                                               # Different types
            if type(lists[0][i]) is int:                                    # Convert whichever value is an int to a list, then compare lists
                compare = compareLists(([lists[0][i]], lists[1][i]))
            else:
                compare = compareLists((lists[0][i], [lists[1][i]]))
        if compare != None: return compare
    return None

def compareInts(ints):
    # Only make a comparison if the values are different
    if ints[0] != ints[1]: 
        return ints[0] < ints[1]
    return None

# https://www.geeksforgeeks.org/merge-sort/
def mergeSort(packets):
    if len(packets) > 1:
        middle = len(packets)//2
        left = packets[:middle]
        right = packets[middle:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if comparePackets((left[i], right[j])):
                packets[k] = left[i]
                i += 1
            else:
                packets[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            packets[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            packets[k] = right[j]
            j += 1
            k += 1
    
if __name__ == "__main__":
    main()
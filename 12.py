def main():
    # Parse input
    with open("inputs/12.txt", "r") as file:
        lines = [line.rstrip() for line in file.readlines()]
        nodes = [[] for _ in lines]
        for i in range(len(lines)):
            for x in range(len(lines[i])):
                nodes[i].append(lines[i][x])
    # Create nodes, identify starting/ending nodes
    startp1 = None
    startp2 = set()
    destination = None
    for i in range(len(nodes)):
        for j in range(len(nodes[i])):
            if nodes[i][j] == "S": # Start
                nodes[i][j] = Node(i,j,1)
                startp1 = nodes[i][j]
                startp2.add(nodes[i][j])
            elif nodes[i][j] == "a": # Start point for part 2
                nodes[i][j] = Node(i,j,1)
                startp2.add(nodes[i][j])
            elif nodes[i][j] == "E": # End
                nodes[i][j] = Node(i,j,26)
                destination = nodes[i][j]
            else: # Regular node
                nodes[i][j] = Node(i,j,ord(nodes[i][j])-96)
    # Set neighbor relations
    for line in nodes:
        for node in line:
            node.setNeighbors(nodes)
    # Solutions
    print("Part1: " + fewestSteps(startp1, nodes, destination))
    print("Part2: " + fewestSteps(startp2, nodes, destination))

# Calculate the fewest steps from starting node(s) to destination
def fewestSteps(start, nodes, destination):
    nodeCosts = {} # Create dictionaries for each node's best path and best path cost
    nodePaths = {}
    for nodeRow in nodes: # For each node, set default best path cost to high number
        for node in nodeRow:
            nodeCosts[node] = 10000
    if type(start) is set: # Set the best path cost of the starting node(s) to 0
        for node in start:
            nodePaths[node] = []
            nodeCosts[node] = 0
    else:
        nodePaths[start] = []
        nodeCosts[start] = 0
    toVisit = start if type(start) is set else {start} # Create a set of what nodes to visit, begin with starting node(s)
    dontVisit = set() # Create a set of nodes that have already been visited
    while toVisit: # While there are still nodes to visit
        current = toVisit.pop() # Pop a random node
        dontVisit.add(current) # Add that node to the don't visit list
        # For each of that node's neighbors, if the path cost of the current node + 1 is less than that neighbor's current path cost, 
        # change best path for that neighbor
        for neighbor in current.neighbors:
            if nodeCosts[neighbor] > nodeCosts[current] + 1:
                nodeCosts[neighbor] = nodeCosts[current] + 1
                nodePaths[neighbor] = [current] + nodePaths[current]
        if not toVisit: # If no more nodes to visit
            for node in dontVisit: # For each node that has been visited
                for neighbor in node.neighbors: # For each of that node's neighbors
                    if neighbor not in dontVisit: # If that neighbor hasn't already been visited, add it to visit list
                        toVisit.add(neighbor)
    return str(nodeCosts[destination])

class Node():
    def __init__(self,i,j,elevation):
        self.i = i
        self.j = j
        self.elev = elevation
    def setNeighbors(self, nodes):
        self.neighbors = []
        # Only add a neighbor if it is at most 1 elevation higher
        if self.i > 0 and self.elev >= nodes[self.i-1][self.j].elev - 1:
            self.neighbors.append(nodes[self.i-1][self.j])
        if self.i + 1 < len(nodes) and self.elev >= nodes[self.i+1][self.j].elev - 1:
            self.neighbors.append(nodes[self.i+1][self.j])
        if self.j > 0 and self.elev >= nodes[self.i][self.j-1].elev - 1:
            self.neighbors.append(nodes[self.i][self.j-1])
        if self.j + 1 < len(nodes[self.i]) and self.elev >= nodes[self.i][self.j+1].elev - 1:
            self.neighbors.append(nodes[self.i][self.j+1])

if __name__ == "__main__":
    main()
from math import trunc

def main():
    print("Part1: " + monkeyRounds(20, 3))
    print("Part2: " + monkeyRounds(10000, 1))

def monkeyRounds(rounds, worryManager):
    monkeys = [] # Create list of monkeys
    with open("inputs/11.txt", "r") as file: # Open input
        currentMonkeyParse = monkeyDict() # Create a new dictionary holding current monkey's init vals
        for line in [line.strip() for line in file.readlines()]: # For each line
            if line == "": # If line is empty, create new monkey and append it to monkey list
                monkeys.append(Monkey(currentMonkeyParse))
                currentMonkeyParse = monkeyDict() # Reset monkey dict
            else: # Line is not empty, grab input
                line = line.split() 
                if line[0].startswith("M"): continue # Monkey number
                elif line[0].startswith("S"): # Monkey starting items
                    for item in line[2:]: # For each starting item
                        currentMonkeyParse["items"].append(int(item.replace(",",""))) # Add item to monkey's item list
                elif line[0].startswith("O"): # Monkey operation
                    if line[5] == "old": # if the operation references itself, it is squaring
                        currentMonkeyParse["operType"] = "**"
                        currentMonkeyParse["operAmt"] = None
                    else:
                        currentMonkeyParse["operType"] = line[4]
                        currentMonkeyParse["operAmt"] = int(line[5])
                elif line[0].startswith("T"): # Monkey's divisible-by number
                    currentMonkeyParse["test"] = int(line[3])
                elif line[1].startswith("t"): # Receiver if divisible
                    currentMonkeyParse["true"] = int(line[5])
                else: # Receiver if not divisible
                    currentMonkeyParse["false"] = int(line[5])
        monkeys.append(Monkey(currentMonkeyParse)) # Add last monkey to list
    # Create mod value if the worryManager is 1
    modValue = 1 
    if worryManager == 1:
        for monkey in monkeys:
            modValue *= monkey.test
    # Play specified rounds
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.family = monkeys
            monkey.play(worryManager, modValue)
    # Identify the two highest inspect counts, and return their product
    inspects = []
    for monkey in monkeys:
        inspects.append(monkey.itemsInspected)
    inspects.sort(reverse=True)
    return str(inspects[0]*inspects[1])

class Monkey():
    def __init__(self, values):
        self.items = values["items"]
        self.operType = values["operType"]
        self.operAmt = values["operAmt"]
        self.test = values["test"]
        self.true = values["true"]
        self.false = values["false"]
        self.itemsInspected = 0
    
    def play(self, worryManager, modValue=None):
        for item in self.items: # For each item
            self.itemsInspected += 1 # Increase inspect count
            if self.operType == "*": # Multiply item by amount
                item *= self.operAmt
            elif self.operType == "+": # Add amount to item
                item += self.operAmt
            else: # Square item
                item *= item
            # If the worryManager is not 1, divide item by worryManager and truncate, else modulo by modValue
            item = trunc(item/worryManager) if worryManager != 1 else item % modValue
            if item % self.test == 0: # Throw to correct receiver
                self.throw(item, self.true)
            else:
                self.throw(item, self.false)
        self.items = [] # Empty monkey's item list, as they have all been thrown
    
    def throw(self, item, receiver):
        self.family[receiver].items.append(item)

def monkeyDict(): # Returns a dictionary that holds a monkey's init vals
    return {
        "items": list(),
        "operType": None,
        "operAmt": None,
        "test": None,
        "true": None,
        "false": None
    }

if __name__ == "__main__":
    main()

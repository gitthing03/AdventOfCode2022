def main():
    output = solution()
    print("Part1: " + output[0])
    print("Part2: " + output[1])

sizesLessThan100K = []
sizes = set()

# Each directory object has a set of sub directories, a set of files, a name, a size, and a parent directory
class Directory(object):
    
    def __init__(self, name, parent=None):
        self.parent = parent
        self.subs = set()
        self.files = set()
        self.name = name
        self.size = 0

    # Add new file to current dir
    def createFile(self, size, name):
        self.files.add(File(size, name))

    # Add new subdir to current dir
    def createSub(self, name):
        self.subs.add(Directory(name, self))

    # Add up the size of all the dir's files
    def calculateFilesSize(self):
        size = 0
        for file in self.files:
            size += file.size
        return size

    # Calculate the size of the dir
    def calculateTotalSize(self):
        # Start with the dir's file size
        total = self.calculateFilesSize()
        # if the dir has subdirs
        if self.subs:
            # Set subdir total to zero
            subTotal = 0
            # for each subdir
            for sub in self.subs:
                # add the size of the subdir to the total
                subTotal += sub.calculateTotalSize()
            # set the size of the dir to the size of the files + the size of the subdirs
            self.size = total+subTotal
        # no subdirs
        else:
            # set size to size of files
            self.size = total
        # if the size is less than 100k, append to list for part 1
        if self.size <= 100000:
            sizesLessThan100K.append(self.size)
        # add size to set for part 2
        sizes.add(self.size)
        # return size of the dir for recursion
        return self.size

# Each file object has a name and a size
class File(object):
    def __init__(self, size, name):
        self.size = size
        self.name = name


def solution():
    # open input
    with open("inputs/07.txt", "r") as file:
        # create base directory obj
        base = Directory(name="/")
        # set currentdir to base
        currentDir = base
        # for each line, skipping the first one
        for line in [line.strip() for line in file.readlines()][1:]:
            # split command into words
            words = line.split(" ")
            # type of info depends on 1st word
            type = words[0]
            # if first word is $, it is a command
            if type == "$":
                # if the second word is 'cd', change dir
                if words[1] == "cd":
                    # if the third word is '..', go to parent dir
                    if words[2] == "..":
                        currentDir = currentDir.parent
                    # else (third word is a name)
                    else:
                        # for each of the current directory's subdirs
                        for sub in currentDir.subs:
                            # find the subdir that matches the given name
                            if sub.name == words[2]:
                                # set current working dir to that sub
                                currentDir = sub
            # if the first word starts with d, it is listing a dir name
            elif type.startswith("d"):
                # create a new dir with that name, as a child to the current dir
                currentDir.createSub(words[1]) # add sub directories to current dir
            # else, first word is a file size
            else:
                # create a new file under the current dir with the name and size
                currentDir.createFile(int(words[0]), words[1])
        
        # -- Part 1
        # calculate the size of each dir
        base.calculateTotalSize()
        # set counter
        total = 0
        # for each dir size that is less than 100k, add to total
        for x in sizesLessThan100K:
            total += x

        # -- Part 2
        # minimum amt to delete is the current empty space substracted from the size of the update
        min = 30000000-(70000000-base.size)
        # lowest amount to delete is by default the base directory (the largest amt)
        lowest = base.size
        # for each directory size
        for size in sizes:
            # if the size is greater than the minimum and less than the current lowest
            if size > min and size < lowest:
                # set lowest to new size
                lowest = size

        # return data for part 1 and 2
        return [str(total), str(lowest)]

if __name__ == "__main__":
    main()
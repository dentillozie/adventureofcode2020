import time

def puzzel1():
    linenumber = 0
    jump = 3
    trees = 0
    index = 0

    fileHandler = open("input", "r")

    listOfLines = fileHandler.readlines()
    length = len(listOfLines[0])-1

    for line in listOfLines:
        if(linenumber > 0):
            if(line[index] == "#"):
                trees = trees+1


        for i in range(0,jump):
            index = index+1
            if(index == length):
              index = 0

        linenumber = linenumber + 1
    print("number of trees in puzzel1:", trees)

def puzzel2(jump, linejump):
    linejump = linejump
    jump = jump
    trees = 0
    index = 0
    lineindex=0

    fileHandler = open("input", "r")

    listOfLines = fileHandler.readlines()
    length = len(listOfLines[0])-1

    amountofline = len(listOfLines)
    while lineindex < amountofline:
        line = listOfLines[lineindex]
        if (lineindex > 0):
            if (line[index] == "#"):
                trees = trees + 1

        for i in range(0, jump):
            index = index + 1
            if (index == length):
               index = 0
        lineindex = lineindex + linejump

    return trees

if __name__ == '__main__':
    dinges = 1

    t = time.process_time()
    puzzel1()
    elapsed_time = time.process_time() - t
    print("benchpress69: ",elapsed_time*10000000, "microsex")

    t = time.process_time()
    dinges = dinges * puzzel2(1,1)
    dinges = dinges * puzzel2(3,1)
    dinges = dinges * puzzel2(5,1)
    dinges = dinges * puzzel2(7,1)
    dinges = dinges * puzzel2(1,2)


    elapsed_time = time.process_time() - t
    print("the product of all dinges:",dinges)
    print("benchpress69: ",elapsed_time*10000000, "microsex")





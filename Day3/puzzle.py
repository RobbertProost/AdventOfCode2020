import os
import sys

def calculateTreesCollisions(treeMap, stepRight, stepDown):
    treeChar = '#'

    lineLength = len(forestMap[0])
    position = 0
    treeCount = 0

    for i in range(stepDown, len(forestMap), stepDown):
        position += stepRight
        position %= lineLength

        if (forestMap[i][position] == treeChar):
            treeCount +=1

    return treeCount

forestMap = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    forestMap = f.readlines()
    forestMap = [x.strip() for x in forestMap]

totalTrees = 0

totalTrees = calculateTreesCollisions(forestMap, 3, 1)

print("Anwser 1: ", totalTrees)

totalTrees *= calculateTreesCollisions(forestMap, 1, 1)
totalTrees *= calculateTreesCollisions(forestMap, 5, 1)
totalTrees *= calculateTreesCollisions(forestMap, 7, 1)
totalTrees *= calculateTreesCollisions(forestMap, 1, 2)

print("Anwser 2: ", totalTrees)
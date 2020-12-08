import os
import sys

def executeProgram(program, indexToSwap = -1):
    acc = 0
    executedInstructions = set()

    instructionPointer = 0
    ended = False

    while (not ended) and (instructionPointer not in executedInstructions):
        executedInstructions.add(instructionPointer)

        if (program[instructionPointer][0] == "acc"):
            acc += int(program[instructionPointer][1])
            instructionPointer += 1
        elif ((program[instructionPointer][0] == "jmp") and (indexToSwap != instructionPointer)):
            instructionPointer += int(program[instructionPointer][1])
        elif ((program[instructionPointer][0] == "nop") and (indexToSwap == instructionPointer)):
            instructionPointer += int(program[instructionPointer][1])
        else:
            instructionPointer += 1

        if (instructionPointer == (len(program))):
            ended = True

    return ended, acc

instructionList = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    inputData = f.readlines()
    instructionList = [x.split() for x in inputData]

ended, acc = executeProgram(instructionList)
print("Part 1: ", acc)

for i in range(len(instructionList)):
    ended, acc = executeProgram(instructionList, i)

    if (ended):
        print("Part 2: ", acc)
        break

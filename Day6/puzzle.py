import os
import sys

inputData = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    inputData = f.read()
    inputData = inputData.split("\n\n")
    inputData = [x.strip() for x in inputData]

sum1 = 0
sum2 = 0

for input in inputData:
    sum1 += len(set(input.replace('\n', '')))

    sets = [set(i) for i in input.split('\n')]
    sum2 += len(set.intersection(*sets))

print("Anwser 1: ", sum1)
print("Anwser 2: ", sum2)
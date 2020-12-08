import os
import sys
import re

def hasShinyGoldBags(bags, currentBag):
    if not currentBag in bags:
        return 0
    
    innerBags = bags[currentBag].split(',')

    containsShinyGoldBags = False

    for innerBag in innerBags:
        match = re.search(r'^(\d) (\w+ \w+) ', innerBag.strip())
        if (match):
            if (match.group(2) == "shiny gold"):
                containsShinyGoldBags = True
            else:
                containsShinyGoldBags |= hasShinyGoldBags(bags, match.group(2))

    return containsShinyGoldBags

def countInnerbags(bags, currentBag):
    if not currentBag in bags:
        return 0
    
    innerBags = bags[currentBag].split(',')

    innerBagCount = 0

    for innerBag in innerBags:
        match = re.search(r'^(\d) (\w+ \w+) ', innerBag.strip())
        if (match):
            innerBagCount += (int(match.group(1)) * countInnerbags(bags, match.group(2))) + int(match.group(1))

    return innerBagCount

inputData = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    inputData = f.read()
    inputData = inputData.split("\n")
    inputData = [x.strip() for x in inputData]
    inputData = dict(x.split(" bags contain ") for x in inputData)

shinyGoldCount = 0
for input in inputData:
    if (hasShinyGoldBags(inputData, input)):
        shinyGoldCount += 1

innerBagCount = countInnerbags(inputData, "shiny gold")

print("Part 1:", shinyGoldCount)
print("Part 2: ", innerBagCount)

import os
import sys
import re

passwordList = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    for line in f:
        line = re.findall(r'(\d+)-(\d+) ([A-Za-z]): (\w+)\n',line)
        passwordList.append(line[0])

nrOfCorrectPasswordsA = 0
nrOfCorrectPasswordsB = 0

for password in passwordList:
    minChar = int(password[0])
    maxChar = int(password[1])
    charToFind = password[2]
    actualPassword = password[3]

    # Zero based indexing
    firstCharPosition = minChar - 1
    secondCharPosition = maxChar - 1

    charsFound = actualPassword.count(charToFind)
    if (int(minChar) <= charsFound <= int(maxChar)):
        nrOfCorrectPasswordsA+=1

    if (firstCharPosition > len(actualPassword) or secondCharPosition > len(actualPassword) ):
        continue

    validPassword = (actualPassword[firstCharPosition] == charToFind) ^ (actualPassword[secondCharPosition] == charToFind)

    if (validPassword):
        nrOfCorrectPasswordsB+=1


print("Correct passwords A: ", nrOfCorrectPasswordsA)
print("Correct passwords B: ", nrOfCorrectPasswordsB)
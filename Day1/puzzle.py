import os
import sys

expenses = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    for line in f:
        line = line.split()
        if line:
            expenses.append(int(line[0]))


resultA = 0
resultB = 0

for i, expense in enumerate(expenses):
    for j, otherExpense in enumerate(expenses, start=i+1):
        if ((expense + otherExpense) == 2020):
            resultA = expense * otherExpense

        for k, anotherExpense in enumerate(expenses, start=j+1):
            if (expense + otherExpense + anotherExpense == 2020):
                resultB = expense * otherExpense * anotherExpense
                break

        if (resultA and resultB):
            break

    if (resultA and resultB):
            break
            
        

print("Result A: ", resultA)
print("Result B: ", resultB)
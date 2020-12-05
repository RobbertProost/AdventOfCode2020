import os
import sys
import math

boardingPasses = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    boardingPasses = f.readlines()
    boardingPasses = [x.strip() for x in boardingPasses]

seatIDs = []
for boardingPass in boardingPasses:

    # Convert to binary number
    boardingPass = boardingPass.replace('B', '1')
    boardingPass = boardingPass.replace('R', '1')
    boardingPass = boardingPass.replace('F', '0')
    boardingPass = boardingPass.replace('L', '0')

    seatID = int(boardingPass, 2)
    seatIDs.append(seatID)

print("Highest ID", max(seatIDs))

seatIDs.sort()

lastSeat = 0
mySeat = 0

for seat in seatIDs:
    if (lastSeat == 0 or seat == lastSeat+1):
        lastSeat = seat
        continue
    elif (seat == lastSeat + 2):
        mySeat = seat - 1
        break

print("My seat: ", mySeat)


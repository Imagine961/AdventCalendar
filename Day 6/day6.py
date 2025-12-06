#setting vars
line1 = []
line2 = []
line3 = []
line4 = []
operation = []
runningTally = 0

#open day 6 input
with open("Day 6/day6input.txt") as file:
    lines = file.readlines()

#adding each row to corresponding array
line1 = lines[0].split()
line2 = lines[1].split()
line3 = lines[2].split()
line4 = lines[3].split()
operation = lines[4].split()

for i, op in enumerate(operation):

    l1 = int(line1[i])
    l2 = int(line2[i])
    l3 = int(line3[i])
    l4 = int(line4[i])

    if op == '*':
        runningTally += (l1*l2*l3*l4)
    elif op == '+':
        runningTally += (l1+l2+l3+l4)

print(runningTally)

### Part 2 ###
#WHAT EVEN IS THIS BRO, its like they just want to see the world burn

runningTally = 0
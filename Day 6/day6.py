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

for i, op in enumerate(operation):
    int1 = 0
    int2 = 0
    int3 = 0
    int4 = 0

    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0

    line12 = line1[i]
    line22 = line2[i]
    line32 = line3[i]
    line42 = line4[i]

    #transforming numbers into a standard form
    l1 = line12.ljust(4, "0")
    l2 = line22.ljust(4, "0")
    l3 = line32.ljust(4, "0")
    l4 = line42.ljust(4, "0")

    #creating new nums based off outline
    num1 = l1[3] + l2[3] + l3[3] + l4[3] 
    num2 = l1[2] + l2[2] + l3[2] + l4[2] 
    num3 = l1[1] + l2[1] + l3[1] + l4[1] 
    num4 = l1[0] + l2[0] + l3[0] + l4[0] 

    int1 = int(num1)
    int2 = int(num2)
    int3 = int(num3)
    int4 = int(num4)

    if op == '*':
        l1 = line12.zfill(4)
        l2 = line22.zfill(4)
        l3 = line32.zfill(4)
        l4 = line42.zfill(4)

        #creating new nums based off outline
        num1 = l1[3] + l2[3] + l3[3] + l4[3] 
        num2 = l1[2] + l2[2] + l3[2] + l4[2] 
        num3 = l1[1] + l2[1] + l3[1] + l4[1] 
        num4 = l1[0] + l2[0] + l3[0] + l4[0] 

        int1 = int(num1)
        int2 = int(num2)
        int3 = int(num3)
        int4 = int(num4)
        runningTally += (int1*int2*int3*int4)
        
    elif op == '+':
        l1 = line12.ljust(4, "0")
        l2 = line22.ljust(4, "0")
        l3 = line32.ljust(4, "0")
        l4 = line42.ljust(4, "0")

        #creating new nums based off outline
        num1 = l1[3] + l2[3] + l3[3] + l4[3] 
        num2 = l1[2] + l2[2] + l3[2] + l4[2] 
        num3 = l1[1] + l2[1] + l3[1] + l4[1] 
        num4 = l1[0] + l2[0] + l3[0] + l4[0] 

        int1 = int(num1)
        int2 = int(num2)
        int3 = int(num3)
        int4 = int(num4)
        runningTally += (int1+int2+int3+int4)

print(runningTally)
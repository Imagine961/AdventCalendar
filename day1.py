input_file = open("day1input.txt", "r")
Input = input_file.read().splitlines()


### BRUTE FORCE SOLUTION ###
test = 0
dial = 50
code = 0

for line in Input:
    if line[0] == "R":
        test = int(line[1:])
        for i in range(test):
            dial += 1
            if dial == 100:
                code += 1
            if dial > 99:
                dial = 0
    elif line[0] == "L":
        test = int(line[1:])
        for i in range(test):
            dial -= 1
            if dial == 0:
                code += 1
            if dial < 0:
                dial = 99


print(code)


### OPTIMIZED SOLUTION ###

for line in Input:
    if line[0] == "R":
        dial += int(line[1:])
    elif line[0] == "L":
        dial -= int(line[1:])
    
    dial = abs(dial) % 100 


    

    print(dial)
with open("Day 7/day7input.txt") as file:
    map = file.readlines()


#GAMEPLAN
'''
1. take the index of s from line 0
2. using the index begin moving through lines until a ^ is reached
3. increase split count by 1
4. when ^ is reached line needs to split 1x index before and 1x index after in the new lines
5. continue moving through lines until you reach end
6. once in the end print count
'''
start = map[0].index("S")

lineLoc = [start]
splitCount = 0
for row in range(1, len(map)):
    line = map[row]

    for i in range(len(line)):
        if line[i] == "^" and (i in lineLoc):
            if (i + 1) not in lineLoc:
                lineLoc.append((i) + 1)
            if (i - 1) not in lineLoc:
                lineLoc.append((i) - 1)
            lineLoc.remove(i)
            splitCount += 1
    
 


print(splitCount)

#THANK YOU RANDOM STRANGER FOR ASSISTANCE ON P2

from collections import defaultdict

timelineBeams = defaultdict(int)
timelineBeams[start] = 1    # one timeline enters at S

for row in range(1, len(map)):
    line = map[row]
    newBeams = defaultdict(int)

    for col, count in timelineBeams.items():
        if col < 0 or col >= len(line):
            continue

        if line[col] == "^":
            # each existing timeline splits into two timelines
            newBeams[col - 1] += count
            newBeams[col + 1] += count
        else:
            # timeline continues straight downward
            newBeams[col] += count

    timelineBeams = newBeams

# Total quantum timelines after exiting the manifold:
print("PART 2:", sum(timelineBeams.values()))
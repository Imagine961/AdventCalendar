#setting up vars
freshIngredientsRange = []
availableIngredients = []
freshIngredients = []
emptyLine = False
rangeFinder = '-'
freshCount = 0
numberOfFreshIngredients = 0

#opening and reading txt
with open("Day 5/day5input.txt") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if rangeFinder in line:
        freshIngredientsRange.append(line)
    else:
        if line != '':
            availableIngredients.append(line)


for line in freshIngredientsRange:
    y = line.split('-')
    lower = int(y[0])
    upper = int(y[1])
    for i in availableIngredients:
        x = int(i)
        if lower <= x <= upper and x not in freshIngredients:
            freshIngredients.append(x)
            freshCount += 1

print(freshCount)

### part 2 ###

#step 1: convert ranges to tuples
ranges = []
for line in freshIngredientsRange:
    low, high = map(int, line.split('-'))
    ranges.append((low, high))

#step 2: sort the ranges
ranges.sort()

#step 3 merge overlapping ranges
merged = []
currentLow, currentHigh = ranges[0]

for low, high in ranges[1:]:
    if low <= currentHigh + 1:
        currentHigh = max(currentHigh, high)
    else:
        merged.append((currentLow, currentHigh))
        currentLow, currentHigh = low, high

merged.append((currentLow, currentHigh))


#step 4 count the unique numbers
freshCount = 0
for low, high in merged:
    freshCount += (high - low + 1)


print(freshCount)

### PART 1 ###

coords = []

# Load red tile coordinates
with open("Day 9/sampleinput.txt") as mapfile:
    for line in mapfile:
        x, y = line.strip().split(",")
        coords.append([int(x), int(y)])

highScore = 0

# Compute largest rectangle using any 2 red tiles
for a in coords:
    for b in coords:
        length = abs(a[0] - b[0]) + 1
        width = abs(a[1] - b[1]) + 1
        area = length * width
        if area > highScore:
            highScore = area

print("Part 1:", highScore)



### PART 2 ###

red_coords = coords.copy()
greenTileCoords = []

# Build boundary green tiles by connecting red tiles
for i in range(len(red_coords)):
    x1, y1 = red_coords[i]
    x2, y2 = red_coords[(i + 1) % len(red_coords)]  # wrap

    # Horizontal
    if y1 == y2:
        step = 1 if x2 > x1 else -1
        for x in range(x1 + step, x2, step):  # exclude endpoints (red)
            greenTileCoords.append([x, y1])

    # Vertical
    elif x1 == x2:
        step = 1 if y2 > y1 else -1
        for y in range(y1 + step, y2, step):  # exclude endpoints
            greenTileCoords.append([x1, y])


INPUT_FILE = "sampleinput.txt"

def part2():
    with open("Day 9/day9input.txt", "r") as f:
        coords = [[int(n) for n in line.strip().split(",")] for line in f]

    max_x = max([c[0] for c in coords])
    max_y = max([c[1] for c in coords])

    # Vertical sweep
    spans = [None for y in range(max_y+2)]
    coords.append(coords[0])
    for i in range(1, len(coords)):
        x1, y1 = coords[i-1]
        x2, y2 = coords[i]
        if x1 > x2: x1,x2 = x2,x1
        if y1 > y2: y1,y2 = y2,y1
        for y in range(y1,y2+1):
            if spans[y] is None:
                spans[y] = [x1, x2]
            else:
                sx1, sx2 = spans[y]
                spans[y] = [min(x1, sx1), max(x2, sx2)]
    coords.pop()

    '''
    for y in range(max_y+2):
        if spans[y] is None:
            print("." * (max_x+2))
        else:
            sx1, sx2 = spans[y]
            print(f"{'.' * sx1}{'X' * (sx2-sx1+1)}{'.' * (max_x+1-sx2)}")
    return
    '''

    def rect_ok(x1, y1, x2, y2):
        if x1 > x2: x1,x2 = x2,x1
        if y1 > y2: y1,y2 = y2,y1
        for y in range(y1, y2+1):
            sx1, sx2 = spans[y]
            if x1 < sx1 or x1 > sx2 or x2 < sx1 or x2 > sx2:
                return False
        return True

    area = 0
    for i in range(len(coords)):
        x1, y1 = coords[i]
        for j in range(i+1, len(coords)):
            x2, y2 = coords[j]
            if x1 != x2 and y1 != y2:
                a = (abs(x1-x2)+1) * (abs(y1-y2)+1)
                if a > area and rect_ok(x1, y1, x2, y2):
                    area = a
    print(area)

part2()
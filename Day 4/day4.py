coordX = 0  # columns
coordY = 0  # rows
rollsAccessed = 0
rollsToBeDeleted = set()
deletedRolls = set()
cellsMarked = False

# load file
with open("Day 4/day4input.txt") as f:
    lines = [list(line.strip()) for line in f]   # convert to 2D array of chars

n_rows = len(lines)
n_cols = len(lines[0])

print(f"rows={n_rows}, cols={n_cols}")


# --- SEARCH FUNCTION FIXED ---
def search_for_symbols(lines, coordX, coordY):
    symbolCount = 0

    # list of 8 relative directions (your original idea)
    directions = [
        ( 0,  1),  # down
        ( 0, -1),  # up
        ( 1,  0),  # right
        (-1,  0),  # left
        ( 1,  1),  # down-right
        ( 1, -1),  # up-right
        (-1,  1),  # down-left
        (-1, -1),  # up-left
    ]

    for dx, dy in directions:
        nx = coordX + dx
        ny = coordY + dy

        # bounds check
        if 0 <= nx < n_cols and 0 <= ny < n_rows:
            if lines[ny][nx] == '@':
                symbolCount += 1

    return symbolCount


# --- FIXED TRAVERSAL LOOP ---
while True:
    cellsMarked = False
    rollsToBeDeleted.clear()

    for coordY in range(n_rows):
        for coordX in range(n_cols):

            current_symbol = lines[coordY][coordX]

            if current_symbol == '@':
                count = search_for_symbols(lines, coordX, coordY)

                if count <= 3:
                    rollsToBeDeleted.add((coordX, coordY))
                    rollsAccessed += 1
                    cellsMarked = True

    if not cellsMarked:
        break

    for x, y in rollsToBeDeleted:
        lines[y][x] = 'X' # mark for deletion



print("Rolls accessed:", rollsAccessed)
print("Number of rolls to be deleted:", len(rollsToBeDeleted))

#### PRETTY SURE IT GIVES ME THE WRONG ANSWER FOR P2 ####
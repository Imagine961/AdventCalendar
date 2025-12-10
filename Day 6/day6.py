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
#WHAT EVEN IS THIS BRO, its like they just want to see the world burn, sorry chat had to take a 4 day bender just to get over it and still cant solve it
#Thanks to Matvei M. for this absolutely ridicoulous solution
def trim(s):
    return "".join(c for c in s if c != " ")

def get_numbers(grid, ops):
    op_i = len(ops) - 1
    res = 0

    # Start the partial value based on last operator
    p = 1 if ops[op_i] == "*" else 0

    for i in range(len(grid[0]) - 1, -1, -1):

        # Build vertical number from column i
        num = "".join(grid[r][i] for r in range(len(grid)))
        num = trim(num)

        if num == "":
            # Only move to next operator if not the first number
            if op_i > 0:
                op_i -= 1
                res += p
                p = 1 if ops[op_i] == "*" else 0
            continue


        if ops[op_i] == "*":
            p *= int(num)
        else:
            p += int(num)

    # Add final accumulation
    res += p
    return res


def main():
    grid = []
    ops = []

    with open("Day 6\day6input.txt", "r") as file:
        for line in file:
            line = line.rstrip("\n")

            if line.startswith("*") or line.startswith("+"):
                ops.extend(line.split())
                continue

            grid.append(line)

    result = get_numbers(grid, ops)
    print(f"\n{result}")


if __name__ == "__main__":
    main()

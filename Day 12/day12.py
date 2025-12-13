answer = 0
with open("Day 12/day12input.txt", "r") as f:
    for parts in [line.strip().split() for line in f if "x" in line]:
        size = [int(x) for x in parts[0][:-1].split("x")]
        area = size[0] * size[1]
        presents = sum([int(x) for x in parts[1:]])
        answer += 1 if area >= presents*9 else 0
print(answer)

## such a stupid but funny final challenge
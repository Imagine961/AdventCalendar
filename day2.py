# Read the entire file as a string
with open("day2input.txt", "r") as f:
    data = f.read().strip()   # .strip() removes newlines/spaces

# Parse into (start, end) integer tuples
ranges = []
for item in data.split(","):
    start, end = item.split("-")
    ranges.append((int(start), int(end)))

print(ranges)

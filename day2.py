# Read file
with open("day2input.txt", "r") as f:
    input_data = f.read().strip()

# Split into list
inputArr = input_data.split(",")

# Counter
invalidID = 0

for s in inputArr:
    before_dash = s.split("-")[0]   # left side of '-'

    # Check for repeated adjacent characters
    for i in range(len(before_dash) - 1):
        if before_dash[i] == before_dash[i + 1]:
            invalidID += 1

print(invalidID)

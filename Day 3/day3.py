
input = open("day3input.txt", "r")
inputLines = input.readlines()
joltage = []

for line in inputLines:
    line = line.strip()

    digits = [int(c) for c in line if c.isdigit()]

    max_two_digit = 0

    for i in range(len(digits)):
        num1 = digits[i] #finding the 10s

        for j in range(i+1, len(digits)):
            num2 = digits[j]  #finding the 1s

            two_digit = num1 * 10 + num2 #10s multiplied by 10 so that it actually carries the value over

            if two_digit > max_two_digit:
                max_two_digit = two_digit

    joltage.append(max_two_digit)

print(joltage)
print(sum(joltage))

### PART 2 ###
'''
im now taking a dynamic approach where eseentially the code reads the length of the string (e.g. 1234 has a length of 4) and then continues moving down the string until it reaches the highest number with enough digits left to fill the length requirement.
(in this situation the length requirement is 12 digits)
'''

lengthRequirement = 12
totalJoltage = 0
for line in inputLines:
    digits = [int(c) for c in line if c.isdigit()]

    if len(digits) < lengthRequirement:
        print("Not enough digits to pick 12")
        continue

    # Reset these FOR EACH LINE
    result = []
    startIndex = 0

    for remaining in range(lengthRequirement, 0, -1):
        endIndex = len(digits) - remaining

        bestNum = -1
        bestIndex = startIndex

        for i in range(startIndex, endIndex + 1):
            if digits[i] > bestNum:
                bestNum = digits[i]
                bestIndex = i

        result.append(bestNum)
        startIndex = bestIndex + 1

    print("Highest 12-digit number:", "".join(map(str, result)))
    totalJoltage += int("".join(map(str, result)))

print("Total Joltage for all lines:", totalJoltage)

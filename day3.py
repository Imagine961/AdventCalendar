
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
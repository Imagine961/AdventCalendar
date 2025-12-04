with open("day2input.txt", "r") as f:
    input = f.read().strip()

ranges = input.split(",")
invalid_ids = []


def isInvalidID(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    
    mid = len(s) // 2

    mid0 = s[:mid]
    mid1 = s[mid:]

    return mid0 == mid1

for x in ranges:
    first, last = map(int, x.split("-"))
    
    for y in range(first, last + 1):
        if isInvalidID(y):
            invalid_ids.append(y)

print(sum(invalid_ids))


###  PART 2 ###

def isInvalidIDv2(n: int) -> bool: #needs to check for just reoccuring numbers
    s = str(n)
    l = len(s)

    for i in range(1, l // 2 + 1):
        if l % i != 0:
            continue # needs to be the same lenghth (future note when im trying to read this code at any point other than 2am)
        chunk = s[:i]
        repeats = l // i

        if s == chunk * repeats and repeats >= 2:
            return True
        
    return False

invalid_ids_v2 = []

for r in ranges:
    first, last = map(int, r.split("-"))
    
    for y in range(first, last + 1):
        if isInvalidIDv2(y):
            invalid_ids_v2.append(y)

print(sum(invalid_ids_v2))

#i hate myself for writing this code at 2am, i accidentally added an additional tab to a return value and this cause the program to miss a total of 41.25 billion numbers
# anyway glad this is over :)
'''
line1 = "0000"
line2 = "64"
line3 = "23"
line4 = "314"

#num1 = 0 + 2 + 6 + 4 = 0264
#num2 = 0 + 1 + 7 + 3 = 0173
#num3 = 0 + 2 + 8 + 2 = 0282
#num4 = 1 + 1 + 9 + 1 = 1191

line1 = line1.ljust(4, "0")
line2 = line2.ljust(4, "0")
line3 = line3.ljust(4, "0")
line4 = line4.ljust(4, "0")
num1 = ""

print(line1)
print(line2)
print(line3)
print(line4)

num1 = line1[3] + line2[3] + line3[3] + line4[3] 
num2 = line1[2] + line2[2] + line3[2] + line4[2] 
num3 = line1[1] + line2[1] + line3[1] + line4[1] 
num4 = line1[0] + line2[0] + line3[0] + line4[0] 

print("-----------------------------")
print(num1)
print(num2)
print(num3)
print(num4)
print("-----------------------------")
print(int(num1))
print(int(num2))
print(int(num3))
print(int(num4))
print("---------------------")
print(int(num1)+int(num2)+int(num3)+int(num4))



line1 = ["123", "328", "51", "64"]
line2 = ["45", "64", "387", "23"]
line3 = ["6", "98", "215", "314"]
line4 = ["0","0","0","0"]
operation = ["*", "+", "*", "+"]

runningTally = 0

for i, op in enumerate(operation):
    int1 = 0
    int2 = 0
    int3 = 0
    int4 = 0

    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0

    line12 = line1[i]
    line22 = line2[i]
    line32 = line3[i]
    line42 = line4[i]

    print(line12)
    print(line22)
    print(line32)
    print(line42)

    maxLen = max(len(line12), len(line22), len(line32), len(line42))
    print(f'maxlen = {maxLen}')

    if op == '*':
        l1 = line12.zfill(maxLen)
        l2 = line22.zfill(maxLen)
        l3 = line32.zfill(maxLen)
        l4 = line42.zfill(maxLen)
        print(f"l1: {l1}")

        #creating new nums based off outline
        if maxLen == 4:
            num1 = l1[3] + l2[3] + l3[3] + l4[3] 
            num2 = l1[2] + l2[2] + l3[2] + l4[2] 
            num3 = l1[1] + l2[1] + l3[1] + l4[1] 
            num4 = l1[0] + l2[0] + l3[0] + l4[0] 
        elif maxLen == 3:
            num1 = l1[2] + l2[2] + l3[2] + l4[2] 
            num2 = l1[1] + l2[1] + l3[1] + l4[1] 
            num3 = l1[0] + l2[0] + l3[0] + l4[0]
            num4 = "000"
        elif maxLen == 2:
            num1 = l1[1] + l2[1] + l3[1] + l4[1] 
            num2 = l1[0] + l2[0] + l3[0] + l4[0]
            num3 = "00"
            num4 = "00"
        else:
            num1 = l1[0] + l2[0] + l3[0] + l4[0]
            num2 = "0"
            num3 = "0"
            num4 = "0"

        int1 = int(num1)
        int2 = int(num2)
        int3 = int(num3)
        int4 = int(num4)
        runningTally += (int1*int2*int3*int4)
        
    elif op == '+':
        l1 = line12.ljust(maxLen, "0")
        l2 = line22.ljust(maxLen, "0")
        l3 = line32.ljust(maxLen, "0")
        l4 = line42.ljust(maxLen, "0")

        #creating new nums based off outline
        if maxLen == 4:
            num1 = l1[3] + l2[3] + l3[3] + l4[3] 
            num2 = l1[2] + l2[2] + l3[2] + l4[2] 
            num3 = l1[1] + l2[1] + l3[1] + l4[1] 
            num4 = l1[0] + l2[0] + l3[0] + l4[0] 
        elif maxLen == 3:
            num1 = l1[2] + l2[2] + l3[2] + l4[2] 
            num2 = l1[1] + l2[1] + l3[1] + l4[1] 
            num3 = l1[0] + l2[0] + l3[0] + l4[0]
            num4 = "000"
        elif maxLen == 2:
            num1 = l1[1] + l2[1] + l3[1] + l4[1] 
            num2 = l1[0] + l2[0] + l3[0] + l4[0]
            num3 = "00"
            num4 = "00"
        else:
            num1 = l1[0] + l2[0] + l3[0] + l4[0]
            num2 = "0"
            num3 = "0"
            num4 = "0"

        int1 = int(num1)
        int2 = int(num2)
        int3 = int(num3)
        int4 = int(num4)
        runningTally += (int1+int2+int3+int4)

print(f"running Tally: {runningTally}")
print("----------------------------")
print(line1)
print(line2)
print(line3)
print(line4)
print("-----------------------------")
print(l1)
print(l2)
print(l3)
print(l4)
print("-----------------------------")
print(num1)
print(num2)
print(num3)
print(num4)
print("-----------------------------")
print(int(num1))
print(int(num2))
print(int(num3))
print(int(num4))
print("---------------------")
print(int(num1)+int(num2)+int(num3)+int(num4))
'''

str = "XX1234"

print(int(str))
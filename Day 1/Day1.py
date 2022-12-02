# Open input.txt to read input

file1 = open("input.txt", "r")
Lines = file1.readlines()

# Adds numbers until it finds a blank line, then take the max of that and the previous max
maxNum = 0
lineSum = 0
# print(Lines)
for line in Lines:
    line = line.strip("\n")
    # print(line)
    if line == "":
        maxNum = max(lineSum, maxNum)

        lineSum = 0
    else:
        lineSum = lineSum + int(line)

print(maxNum)
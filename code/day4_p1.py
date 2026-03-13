def readinput(source):
    with open(source, "r") as file:
        arrays = []
        for line in file:
            temp = list(line.rstrip().replace("@", "1").replace(".", "0"))
            arrays.append([int(x) for x in temp])
    return arrays

arr = readinput("day4_input.txt")
#arr = readinput("test.txt")
#print(arr)

total = 0
valid = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        rolls = 0
        for k in range(i-1, i+2):
            for l in range(j-1, j+2):
                try:
                    if k >= 0 and l >= 0 and arr[k][l] == 1:
                        rolls += 1
                except:
                    pass
        if rolls < 5 and arr[i][j] == 1:
            total += 1
            valid.append([i, j])

print(total)
#print(valid)
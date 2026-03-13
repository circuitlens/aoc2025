def readinput(source):
    with open(source, "r") as file:
        for line in file:
            raw = line.rstrip().split(",")
        inter = []
        for i in raw:
            temp = i.split("-")
            inter.append([int(temp[0]), int(temp[1])])
    return inter

intervals = readinput("day2_input.txt")
#intervals = readinput("test.txt")

total = 0
for i in intervals:
    for j in range(i[0], i[1]+1):
        num = str(j)
        if len(num) % 2 == 0:
            h1 = num[:len(num)//2]
            h2 = num[len(num)//2:]
            if h1 == h2:
                total += j

print(total)
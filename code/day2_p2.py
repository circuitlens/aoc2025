import textwrap 

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
invalid = []
for i in intervals:
    for j in range(i[0], i[1]+1):
        num = str(j)
        lennum = len(num)
        for k in range(1, lennum):
            if lennum % k == 0:
                elem = textwrap.wrap(num, k)
                if len(set(elem)) == 1:
                    #total += j
                    invalid.append(j)
                    print(j)
invalid = set(invalid)
total = sum(invalid)
print("")
print(total)
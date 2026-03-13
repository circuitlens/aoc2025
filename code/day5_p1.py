def readinput(source):
    with open(source, "r") as file:
        o_ranges = []
        o_numbers = []
        for line in file:
            if "-" in line:
                temp = line.rstrip().split("-")
                temp[0], temp[1] = int(temp[0]), int(temp[1])
                o_ranges.append(temp)
            elif line.rstrip() != "":
                o_numbers.append(int(line.rstrip()))
    return o_ranges, o_numbers

rng, num = readinput("day5_input.txt")
#rng, num = readinput("test.txt")

fresh = []

for i in num:
    for j in rng:
        if i in range(j[0], j[1]+1) and i not in fresh:
            print(i)
            fresh.append(i)
print(len(fresh))
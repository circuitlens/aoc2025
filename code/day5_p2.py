def readinput(source):
    with open(source, "r") as file:
        o_ranges = []
        for line in file:
            if "-" in line:
                temp = []
                temp = line.rstrip().split("-")
                temp[0], temp[1] = int(temp[0]), int(temp[1])
                o_ranges.append((temp[0], temp[1]))
    return o_ranges

rng = readinput("day5_input.txt")
#rng = readinput("test.txt")

rng.sort()
total = 0
c_start, c_end = rng[0]
for start, end in rng[1:]:
    if start <= c_end + 1:
        c_end = max(c_end, end)
    else:
        total += c_end - c_start + 1
        c_start, c_end = start, end
total += c_end - c_start + 1
print(total)
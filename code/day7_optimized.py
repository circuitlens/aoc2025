def readinput(source):
    with open(source, "r") as file:
        lines = []
        for line in file:
            lines.append(list(line.rstrip()))
        for l in range(len(lines)):
            for c in range(len(lines[l])):
                if lines[l][c] == ".":
                    lines[l][c] = 0
    return lines

ln = readinput("day7_input.txt")
#ln = readinput("test.txt")

splits = 0
timelines = []
for i in range(len(ln[0])):
    timelines.append(0)

for ind in range(len(ln)):
    item=ln[ind]
    for ch in range(len(item)):
        char = item[ch]
        try:
            if char == "S":
                timelines[ch] = 1
            elif char == "^" and timelines[ch] != 0:
                splits += 1
                timelines[ch+1] += timelines[ch]
                timelines[ch-1] += timelines[ch]
                timelines[ch] = 0
                print(splits)
                print(timelines)
        except:
            pass
print(ln)
print(timelines)
print("splits: ", splits)
print("timelines: ", sum(timelines))

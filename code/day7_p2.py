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
result = []
for i in range(len(ln[0])):
    result.append(0)
for ind in range(len(ln)):
    item=ln[ind]
    for ch in range(len(item)):
        char = item[ch]
        try:
            if char == "S":
                result[ch] = 1
            elif char == "^" and type(ln[ind-1][ch]) == int:
                result[ch+1] += result[ch]
                result[ch-1] += result[ch]
                result[ch] = 0
        except:
            pass
print(result)
timelines = sum(result)
#timelines = 0
#for num in ln[len(ln)-1]:
#    if type(num) == int:
#        timelines += num
#for a in range(len(ln)):
#    for b in range(len(ln[a])):
#        ln[a][b] = str(ln[a][b])

#for item in ln: print(item)
print(timelines)


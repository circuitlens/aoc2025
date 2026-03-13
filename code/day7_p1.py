def readinput(source):
    with open(source, "r") as file:
        lines = []
        for line in file:
            lines.append(list(line.rstrip()))
    return lines

#ln = readinput("day7_input.txt")
ln = readinput("test.txt")

splitcount = 0
for ind in range(len(ln)):
    item=ln[ind]
    for ch in range(len(item)):
        char = item[ch]
        try:
            if char == "S":
                ln[ind+1][ch] = "|"
            elif char == "^" and ln[ind-1][ch] == "|":
                ln[ind][ch+1] = "|"
                ln[ind][ch-1] = "|"
                ln[ind+1][ch+1] = "|"
                ln[ind+1][ch-1] = "|"
                splitcount += 1
                print(char)
            elif char == "|" and ln[ind+1][ch] == ".":
                ln[ind+1][ch] = "|"
        except:
            pass
            #print("error")
for item in ln: print(item)
print(splitcount)


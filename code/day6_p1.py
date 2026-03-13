def readinput(source):
    with open(source, "r") as file:
        lines = []
        problems = []
        for line in file:
            lines.append(line.strip().split())

        for i in range(len(lines[0])):
            temp = []
            temp.append(lines[len(lines)-1][i])
            for j in range(len(lines)-1):
                temp.append(lines[j][i])
                print(temp)
            
            problems.append(temp)
    print(problems)
    return problems

#prob = readinput("day6_input.txt")
prob = readinput("test.txt")
print(prob)
total = 0
for k in prob:
    #print(k)
    value = int(k[1])
    for l in range(2, len(k)):
        print(l)
        if k[0] == "+":
            value += int(k[l])
        elif k[0] == "*":
            value *= int(k[l])
    total += value
    #print(value)
print("")
print(total)
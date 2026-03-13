def readinput(source):
    with open(source, "r") as file:
        lines = []
        for line in file:
            lines.append(line.rstrip())
    return lines

def ceph(inp):
    output = []
    #print(inp)
    outtemp2 = []
    for char in range(len(max(inp, key=len))):
        outtemp = ""
        for string in range(len(inp)-1):
            try:
                outtemp += inp[string][char]
            except:
                pass
        outtemp2.append(outtemp.strip())
    #print(outtemp2)
    operand = inp[len(inp)-1].split()
    #print(operand)
    outtemp3 = [operand[0]]
    operand_count = 0
    outtemp2.append("")
    print(outtemp2)
    for num in outtemp2:
        if num == "" or num is None:
            output.append(outtemp3)
            print(outtemp3)
            operand_count += 1
            try:
                outtemp3 = [operand[operand_count]]
            except:
                operand_count -= 1
                outtemp3 = operand[operand_count]
        else:
            outtemp3.append(num)
    print(output)
    return output

prob = ceph(readinput("day6_input.txt"))
#prob = ceph(readinput("test.txt"))

print(prob)
total = 0
for k in prob:
    print(k)
    value = int(k[1])
    for l in range(2, len(k)):
        #print(l)
        if k[0] == "+":
            value += int(k[l])
        elif k[0] == "*":
            value *= int(k[l])
    total += value
    print(value)
print("")
print(total)
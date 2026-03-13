def readinput(source):
    with open(source, "r") as file:
        lines = []
        for line in file:
            line = line.strip().split(" ")
            lines.append(line)
    return lines

def all_combinations(lst):
    result = [[]]
    for elem in lst:
        result += [sub + [elem] for sub in result]
    return result

#lines = readinput("test.txt")
lines = readinput("day10_input.txt")

total_presses = 0
for ln in lines:
    lght = ln[0]
    lights = []
    shortest = len(ln)-2
    for char in lght:
        if char == "#":
            lights.append(1)
        elif char == ".":
            lights.append(0)
    buttons = []
    for btn in range(1, len(ln)-1):
        but = ln[btn].strip()[1:-1].split(",")
        for i in range(len(but)): but[i] = int(but[i])
        buttons.append(but)
    options = all_combinations(buttons)
    for opt in options:
        pattern = []
        for i in range(len(lights)):
            pattern.append(0)
        #print(lights)
        for button in opt:
            #print(pattern)
            for num in range(len(button)):
                #print(button, num)
                pattern[button[num]] += 1
        for j in range(len(pattern)):
            pattern[j] = pattern[j]%2
        if pattern == lights and len(opt) < shortest:
            shortest = len(opt)
    total_presses += shortest
print(total_presses)

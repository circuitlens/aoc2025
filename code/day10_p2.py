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

def solve_layer(jolt, ln):
    joltages = [x%2 for x in jolt]
    shortest = sum(jolt)
    buttons = []
    for btn in range(1,len(ln)-1):
        but = ln[btn].strip()[1:-1].split(",")
        for i in range(len(but)): but[i]=int(but[i])
        buttons.append(but)
    options = all_combinations(buttons)
    best_pattern = None
    best_option = None
    for opt in options:
        if not len(opt)>shortest:
            pattern = [0]*len(jolt)
            for button in opt:
                for num in range(len(button)):
                    pattern[button[num]] += 1
            pattern_mod = [x%2 for x in pattern]
            if pattern_mod == joltages and len(opt)<shortest:
                shortest = len(opt)
                best_pattern = pattern[:]
                best_option = opt
    remaining = [jolt[i]-best_pattern[i] for i in range(len(jolt))]
    return shortest, remaining, best_option


total_presses = 0
for ln in lines:
    remaining_joltage = [int(x) for x in ln[-1].strip()[1:-1].split(",")]
    weight = 1
    #print(remaining_joltage)
    while sum(remaining_joltage) != 0:
        shortest, remaining_joltage, best_option = solve_layer(remaining_joltage, ln)
        total_presses += shortest * weight
        remaining_joltage = [x//2 for x in remaining_joltage]
        #print(total_presses, remaining_joltage, shortest*weight, best_option)
        weight *= 2
print("")
print(total_presses)
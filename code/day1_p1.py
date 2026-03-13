def readinput(source):
    with open(source, "r") as file:
        commands = []
        for line in file:
            line = line.rstrip()
            commands.append([line[0], int(line.replace(line[0], ""))])
    return commands

cmd = readinput("day1_input.txt")
value = 50
times_zero = 0
for i in cmd:
    if i[0] == "R":
        value += i[1]
    else:
        value -= i[1]
    
    while not 0 <= value <= 99:
        if value > 99: 
            value -= 100
        elif value < 0: 
            value += 100

    if value == 0: 
        times_zero += 1

print(times_zero)
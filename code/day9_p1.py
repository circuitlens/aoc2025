def readinput(source):
    with open(source, "r") as file:
        lines = []
        for line in file:
            line = line.strip().split(",")
            line[0], line[1] = int(line[0]), int(line[1])
            lines.append(line)
    return lines

#points = readinput("test.txt")
points = readinput("day9_input.txt")

print(points)
highest_area = 0
for v1 in points:
    for v2 in points:
        x = 0
        y = 0
        if v2[0] < v1[0]:
            x = v1[0]-v2[0]+1
        else:
            x = v2[0]-v1[0]+1
        if v2[1] < v1[1]:
            y = v1[1]-v2[1]+1
        else:
            y = v2[1]-v1[1]+1
        #print(x, y)
        temp = x*y
        if temp > highest_area:
            highest_area = temp
print(highest_area)
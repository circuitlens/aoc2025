#very bad, please optimize later

def readinput(source):
    with open(source, "r") as file:
        lines = []
        for line in file:
            lines.append(line.strip().split(","))
        for a in range(len(lines)):
            for b in range(len(lines[a])):
                lines[a][b] = int(lines[a][b])
    return lines

#points = readinput("test.txt")
#connections = 10
points = readinput("day8_input.txt")
connections = 1000

dists = []
for a in range(len(points)):
    for b in range(a+1, len(points)):
        p1 = points[a]
        p2 = points[b]
        dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2
        dists.append([dist, p1, p2])

dists = sorted(dists, key=lambda x: x[0])
#for i in range(len(dists)): print(dists[i])

conns = dists[:connections]

"""
circuits = []
#for i in range(len(conns)): 
#    circuits.append([conns[i]])
#    print(conns[i])

for j in range(1, len(conns)):
    dp1 = conns[j][1]
    dp2 = conns[j][2]
    contained_in = []
    for c in range(len(circuits)):
        for item in range(len(circuits[c])):
            entry = circuits[c][item]
            if dp1 == entry[1] or dp1 == entry[2] or dp2 == entry[1] or dp2 == entry[2]:
                contained_in.append(c)
    if contained_in == []:
        circuits.append([conns[j]])
    else:
        new_circuit = [conns[j]]
        new_circuit = []
        for index in reversed(sorted(list(set(contained_in)))):
            new_circuit += circuits[index]
            circuits.pop(index)
        circuits.append(new_circuit)
"""

circuits = []
for dist, p1, p2 in conns:
    p1t = tuple(p1)
    p2t = tuple(p2)
    contained_in = []
    for i, circuit in enumerate(circuits):
        if p1t in circuit or p2t in circuit:
            contained_in.append(i)
    if not contained_in:
        circuits.append(set([p1t, p2t]))
    else:
        new_circuit = set([p1t, p2t])
        for i in reversed(sorted(contained_in)):
            new_circuit |= circuits[i]
            circuits.pop(i)
        circuits.append(new_circuit)

circuits = sorted(circuits, key=len, reverse = True)
print("")
for k in range(3): 
    print(circuits[k])

"""
result = 0
for k in range(0, 3):
    circ = circuits[k] 
    points_in_circuit = []
    for point in circ:
        if point[1] not in points_in_circuit:
            points_in_circuit.append(point[1])
        if point[2] not in points_in_circuit:
            points_in_circuit.append(point[2])
    if result == 0:
        result = len(points_in_circuit)
    else:
        result *= len(points_in_circuit)
"""

result = 0
for k in range(0, 3):
    if result == 0:
        result = len(circuits[k])
    else:
        result *= len(circuits[k])
print(result)
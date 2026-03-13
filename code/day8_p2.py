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

circuits = []
final_connection = None
for dist, p1, p2 in dists:
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
    if len(circuits) == 1 and len(circuits[0]) == len(points):
        final_connection = [p1t, p2t]
        break

final_conn_x = final_connection[0][0] * final_connection[1][0]

circuits = sorted(circuits, key=len, reverse = True)
#print("")
#print(circuits)
print("")
print(final_connection)
print(final_conn_x)
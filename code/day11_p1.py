def readinput(source):
    with open(source, "r") as file:
        lines = {}
        for line in file:
            line = line.strip().split(":")
            lines[line[0]] = line[1].strip().split()
    return lines

#racks = readinput("test.txt")
racks = readinput("day11_input.txt")

all_paths = []

def find_paths(graph, node, path):
    path.append(node)
    if graph[node] == ["out"]:
        all_paths.append(path.copy())
    else:
        for nxt in graph[node]:
            find_paths(graph, nxt, path)
    path.pop()

find_paths(racks, "you", [])
print(all_paths)
print("")
print(len(all_paths))
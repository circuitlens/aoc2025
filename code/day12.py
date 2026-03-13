def readinput(source):
    with open(source, "r") as file:
        lines = file.readlines()
    shapes = []
    areas = []
    ln = 0
    
    while ln < len(lines):
        line = lines[ln].strip()
        if line.endswith(":") and line[:-1].isdigit():
            ln += 1
            shape = []
            while ln < len(lines):
                row = lines[ln].rstrip("\n")
                if row.strip() == "":
                    break
                shape.append(list(row))
                ln += 1
            shapes.append(shape)
        ln += 1

    for line in lines:
        line = line.strip()
        if "x" in line and ":" in line:
            left, right = line.split(":")
            left = left.strip()
            right = right.strip()
            W, H = left.split("x")
            W = int(W)
            H = int(H)
            counts = [int(x) for x in right.split()]
            areas.append([(W, H)] + counts)
    return shapes, areas

#shapes, areas = readinput("test.txt")
shapes, areas = readinput("day12_input.txt")
"""
newshapes = []
for shape in shapes:
    newshapes.append([shape,
    (list(zip(*shape[::-1]))),
    (shape[::-1]),
    (list(zip(*shape)[::-1]))])
shapes = newshapes[:]

def dfs(shapes, areas):
    for area in areas:
        grid = [["." for i in range(area[0][0])] for j in range(area[0][1])]
        for k in range(1, len(area)+1):
            for l in range(len(k)):
                gridstate = grid[:]
                shape = shapes[k-1][l]
                for m in range(len(shape[0])):
                    for n in range(len(shape)):
"""                     

#hacky solution, why does this even work ???

shapeareas = []
for shape in shapes:
    shapeareas.append(sum(row.count("#") for row in shape))

valid = 0
for area in areas:
    surface = area[0][0] * area[0][1]
    shapes_total_area = 0
    for i in range(1, len(area)):
        shapes_total_area += area[i]*shapeareas[i-1]
    if shapes_total_area <= surface:
        valid += 1

print(valid)
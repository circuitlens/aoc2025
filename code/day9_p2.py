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

row_intervals = []
col_intervals = []
for i in range(len(points)):
    x1, y1 = points[i]
    x2, y2 = points[(i+1) % len(points)]
    if x1 == x2:
        col_intervals.append((min(y1, y2), max(y1, y2), x1))
    else:
        row_intervals.append((min(x1, x2), max(x1, x2), y1))


highest_area = 0

rectangles = []

for v1 in points:
    for v2 in points:
        left = min(v1[0], v2[0])
        right = max(v1[0], v2[0])
        top = min(v1[1], v2[1])
        bottom = max(v1[1], v2[1])
        lrtb = [left, right, top, bottom]

        width = right - left + 1
        height = bottom - top + 1
        area = width * height

        corners = [[left, top], [left, bottom], [right, top], [right, bottom]]
        rectangles.append([lrtb, corners, area])

for rect in rectangles:
    valid = True
    left, right, top, bottom = rect[0]

    for x_edge_rect in (left, right):
        for x1, x2, y_edge in row_intervals:
            if top < y_edge < bottom and x1 <= x_edge_rect <= x2:
                valid = False
                break
        if not valid:
            break

    if valid:
        for y_edge_rect in (top, bottom):
            for y1, y2, x_edge in col_intervals:
                if left < x_edge < right and y1 <= y_edge_rect <= y2:
                    valid = False
                    break
            if not valid:
                break
    if valid and rect[2] > highest_area:
        highest_area = rect[2]
        print(rect[1])

print("")
print(highest_area)
  
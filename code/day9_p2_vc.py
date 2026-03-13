def readinput(source):
    with open(source, "r") as file:
        lines = []
        for line in file:
            line = line.strip().split(",")
            lines.append((int(line[0]), int(line[1])))
    return lines


# -------------------------------------------------------
#    FAST ORTHOGONAL POINT-IN-POLYGON
# -------------------------------------------------------

def build_vertical_edges(poly):
    """Given ordered polygon vertices, return list of vertical edges.
       Each edge is (x, y_low, y_high)."""
    V = []
    m = len(poly)
    for i in range(m):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % m]
        if x1 == x2:
            # vertical edge
            lo = min(y1, y2)
            hi = max(y1, y2)
            V.append((x1, lo, hi))
    return V


def point_in_poly(px, py, vertical_edges):
    """Ray cast to the right. py must be inside edge's open interval (lo < py <= hi or similar)."""
    inside = False
    for x, lo, hi in vertical_edges:
        # Check if ray at py crosses edge:
        # For orthogonal polygons the conventional robust rule is:
        #     lo <= py < hi    (half-open interval)
        if lo <= py < hi:
            if px < x:      # edge is to the right of the point
                inside = not inside
    return inside


# -------------------------------------------------------
#                 PART 2 SOLVER (FAST)
# -------------------------------------------------------

def part2(points):
    reds = points[:]              # polygon vertices in order
    redset = set(reds)

    # Build vertical edges of polygon
    vertical_edges = build_vertical_edges(reds)

    best = 0
    n = len(reds)

    for i in range(n):
        x1, y1 = reds[i]

        for j in range(i + 1, n):
            x2, y2 = reds[j]

            xmin = min(x1, x2)
            xmax = max(x1, x2)
            ymin = min(y1, y2)
            ymax = max(y1, y2)

            # area inclusive of tiles
            area = (xmax - xmin + 1) * (ymax - ymin + 1)
            if area <= best:
                continue

            # Check the 4 corners of the rectangle:
            # If all are inside/on-boundary, the whole rectangle is inside.
            ok = True
            for cx, cy in ((xmin, ymin), (xmin, ymax),
                           (xmax, ymin), (xmax, ymax)):
                if not point_in_poly(cx + 0.5, cy + 0.5, vertical_edges):
                    ok = False
                    break

            if ok:
                best = area

    return best


# -------------------------------------------------------
# Example Test (should print 24)
# -------------------------------------------------------


points = readinput("day9_input.txt")
print(part2(points))  # expected: 24

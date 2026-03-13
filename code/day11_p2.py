def readinput(source):
    with open(source, "r") as file:
        lines = {}
        for line in file:
            line = line.strip().split(":")
            lines[line[0]] = line[1].strip().split()
    return lines

#racks = readinput("test.txt")
racks = readinput("day11_input.txt")

memo = {}
visiting = set()

def count_paths(graph, start, end):
    if (start, end) in memo:
        return memo[(start, end)]

    if start == end:
        memo[(start, end)] = 1
        return 1

    if start not in graph:
        memo[(start, end)] = 0
        return 0

    if start in visiting:
        return 0

    visiting.add(start)

    total = 0
    for nxt in graph[start]:
        total += count_paths(graph, nxt, end)

    visiting.remove(start)

    memo[(start, end)] = total
    return total

results = {}

svr_dac = count_paths(racks, "svr", "dac") 
dac_fft = count_paths(racks, "dac", "fft") 
fft_out = count_paths(racks, "fft", "out") 
svr_fft = count_paths(racks, "svr", "fft") 
fft_dac = count_paths(racks, "fft", "dac") 
dac_out = count_paths(racks, "dac", "out")

all_paths_count = (svr_dac * dac_fft * fft_out) + (svr_fft * fft_dac * dac_out)

print(all_paths_count)

def readinput(source):
    with open(source, "r") as file:
        arrays = []
        for line in file:
            arrays.append(line.rstrip())
    return arrays

arr = readinput("day3_input.txt")
#arr = readinput("test.txt")

total = 0
for i in arr:
    digits = 12
    biggest = ""
    biggest_temp = [0, -1]
    for j in range(0, digits):
        biggest_prev = biggest_temp
        biggest_temp = [0, -1]
        for k in range(biggest_prev[1], len(i)-(digits-len(biggest)-1)):
            if int(i[k]) > biggest_temp[0] and k > biggest_prev[1]:
                biggest_temp = [int(i[k]), k]
        biggest += str(biggest_temp[0])
    total += int(biggest)
    print(biggest)

print("")
print(total)
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
    biggest_1 = [0, 0]
    biggest_2 = [0, 0]
    biggest = ""

    for j in range(0, len(i)-1):
        if int(i[j]) > biggest_1[0]:
            biggest_1 = [int(i[j]), j]

    for k in range(biggest_1[1]+1, len(i)):
        if int(i[k]) > biggest_2[0]:
            biggest_2 = [int(i[k]), k]

    biggest += str(biggest_1[0])
    biggest += str(biggest_2[0])
    total += int(biggest)
    print(biggest)

print("")
print(total)
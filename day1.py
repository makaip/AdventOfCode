data = open('info.txt')
array = []
numbers = []
numbersfirst = []
numberslast = []
totalset = []
final = 0

for line in data:
    array.append(line)

for line in array:
    for char in line:
        if (char.isdigit()):
            numbers.append(char)
    numbersfirst.append(numbers[0])
    numbers.reverse()
    numberslast.append(numbers[0])
    numbers.clear()

for x in range(len(array)):
    totalset.append(str(numbersfirst[x]) + str(numberslast[x]))

for x in totalset:
    final = final + int(x)

print(final)



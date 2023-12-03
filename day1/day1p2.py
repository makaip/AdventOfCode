data = open("info.txt")
numbers = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero" ]

array, sets, numbersfirst, numberslast = [], [], [], []
for line in data:
    array.append(line)

for line in array:
    indexes = []
    for num in numbers:
        if line.find(num) != -1:
            indexes.append([line.find(num), num])
    sets.append(indexes)

print(sets)

for i in range(10):
    for j in range(len(indexes)):
        indexes[j][1] = indexes[j][1].replace(numbers[i+10], numbers[i])


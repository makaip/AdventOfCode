data = open("info.txt")
numbers = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
array, sets, sussy, help = [], [], [], []

for line in data:
    array.append(line)

for line in array:
    indexes = []
    for num in numbers:
        if line.find(num) != -1:
            indexes.append([line.find(num), num])
    sets.append(indexes)

def firstItem(ls):
    return ls[0][0]

for i in sets:
    i.sort(key=lambda x:x[0])

for i in range(len(sets)):
    for j in range(len(sets[i])):
        sets[i][j][1] = sets[i][j][1].replace("one", "1")
        sets[i][j][1] = sets[i][j][1].replace("two", "2")
        sets[i][j][1] = sets[i][j][1].replace("three", "3")
        sets[i][j][1] = sets[i][j][1].replace("four", "4")
        sets[i][j][1] = sets[i][j][1].replace("five", "5")
        sets[i][j][1] = sets[i][j][1].replace("six", "6")
        sets[i][j][1] = sets[i][j][1].replace("seven", "7")
        sets[i][j][1] = sets[i][j][1].replace("eight", "8")
        sets[i][j][1] = sets[i][j][1].replace("nine", "9")
        sets[i][j][1] = sets[i][j][1].replace("zero", "0")

# print(sets[25])

final = 0
amognus, sus, blub = [], [], []

for i in sets:
    amognus.append(i[0][1])

for i in sets:
    i.reverse()
    sus.append(i[0][1])

for i in range(len(sets)):
    blub.append(int(amognus[i] + sus[i]))

for i in blub:
    final = final + int(i)
# print(final)

bubby = 0
for baka in array:
    for suss in baka:
        print(suss, end="")
    bubby = bubby + 1
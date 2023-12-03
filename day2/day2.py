data, game = open('day2/input2.txt'), []

for line in data:
    game.append(line.strip())

blub, chub, glub = [], [], []
for i in game:
    blub.append(i.split(": "))

for j in blub:
    j[1] = j[1].split("; ")

for k in blub:
    chub = []
    for l in k[1]:
        l = l.split(", ")
        chub.append(l)
    glub.append(chub)

chrub, grub, brub = [], [], []
for i in glub:
    rub, gub, bub = [], [], []
    for j in i:
        for k in j:
            if "red" in k:
                rub.append(int(k.strip(" red")))
            elif "green" in k:
                gub.append(int(k.strip(" green")))
            elif "blue" in k:
                bub.append(int(k.strip(" blue")))
            else:
                print("Somethings probably wrong here")
    chrub.append(rub)
    grub.append(gub)
    brub.append(bub)

total = 0

for i in chrub:
    i.sort()
    i.reverse()

for i in grub:
    i.sort()
    i.reverse()

for i in brub:
    i.sort()
    i.reverse()

for i in range(len(game)):
    linetotal = int(chrub[i][0]) * int(grub[i][0]) * int(brub[i][0])
    # print(str(i), chrub[i][0], grub[i][0], brub[i][0], linetotal)
    total = total + linetotal

print(total)

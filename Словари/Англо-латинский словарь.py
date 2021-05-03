#Задача «Англо-латинский словарь»
# 3
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa

latin_english = {}
for i in range(int(input())):
    line = input().split()
    line.pop(1)
    for j in range(len(line)):
        a = line[j]
        if a[-1]==',':
            line[j] = a[:-1]
    for f in range(1, len(line)):
        if line[f] in latin_english:
            latin_english[line[f]] = latin_english[line[f]]+', ',line[0]
        else:
            latin_english[line[f]] = line[0]
a = []
for key, val in latin_english.items():
    a.append((key, val))
a = sorted(a)
for i in a:
    print(i[0], ' - ', i[1])

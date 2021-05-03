#Задача «Родословная: предки и потомки»
#Условие
#Даны два элемента в дереве. Определите, является ли один из них потомком другого.

#Во входных данных записано дерево в том же формате, что и в предыдущей задаче
#Далее идет число запросов K. В каждой из следующих K строк, содержатся
#имена двух элементов дерева.

#Для каждого такого запроса выведите одно из трех чисел: 1, если первый
#элемент является предком второго, 2, если второй является предком первого или 0,
#если ни один из них не является предком другого.
# 9
# Alexei Peter_I
# Anna Peter_I
# Elizabeth Peter_I
# Peter_II Alexei
# Peter_III Anna
# Paul_I Peter_III
# Alexander_I Paul_I
# Nicholaus_I Paul_I
# 3
# Anna Nicholaus_I
# Peter_II Peter_I
# Alexei Paul_I

child_parents = {}
n = int(input())

for i in range(n-1):
    line = input().split()
    child_parents[line[0]] = line[1]

for i in range(int(input())):
    line = input().split()
    key1 = line[0]
    key2 = line[1]
    i = 0
    while True:
        if key2 in child_parents:
            key2 = child_parents[key2]
            if key2 == line[0]:
                i = 1
                break
        if key1 in child_parents:
            key1 = child_parents[key1]
            if key1 == line[1]:
                i = 2
                break
        if (key1 not in child_parents) and (key2 not in child_parents):
            break
    print(i, end=' ')
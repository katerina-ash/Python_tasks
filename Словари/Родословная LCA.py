#Задача «Родословная: LCA»
#Условие
#В генеалогическом древе определите для двух элементов их наименьшего общего
#предка (Lowest Common Ancestor). Наименьшим общим предком элементов A и B
#является такой элемент C, что С является предком A, C является предком B,
#при этом глубина C является наибольшей из возможных. При этом элемент
#считается своим собственным предком.

#Формат входных данных аналогичен предыдущей задаче

#Для каждого запроса выведите наименьшего общего предка данных элементов.

child_parents = {}
n = int(input())

for i in range(n-1):
    line = input().split()
    child_parents[line[0]] = line[1]

for i in range(int(input())):
    line = input().split()
    child1 = line[0]
    child2 = line[1]
    while True:
        parents1 = child_parents[child1]
        while child2 in child_parents:
            parents2 = child_parents[child2]
            if parents1 == parents2:
                break
            child2 = parents2
        if parents1 == parents2:
            break
        child1 = parents1
    print(parents2)

#Задача «Четные индексы»
#Условие
#Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
A = input().split()
for s in range(len(A)):
    A[s] = int(A[s])
for i in range(len(A)):
    if i % 2 == 0:
        print(A[i], end=' ')
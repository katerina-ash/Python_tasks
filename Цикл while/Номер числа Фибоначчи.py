#Задача «Номер числа Фибоначчи»
#Условие
#Дано натуральное число A. Определите, каким по счету числом Фибоначчи
#оно является, то есть выведите такое число n, что φn = A. Если А не является
#числом Фибоначчи, выведите число -1.
A = int(input())
f1 = 0
fsum = 0
f2 = 1
i = 0
while fsum < A:
    fsum = f1 + f2
    f1 = f2
    f2 = fsum
    i += 1
    if A == f2:
        print(i)
        break
if A < 0 or A != f2:
    print(-1)
elif A == 0:
    print(0)
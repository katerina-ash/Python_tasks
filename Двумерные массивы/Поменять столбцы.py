# Задача «Поменять столбцы»
# Условие
# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
# Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
# Решение оформите в виде функции swap_columns(a, i, j).
# 3
# 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 0
# 1
n = int(input('Введите первое значение размера массива: '))
m = int(input('Введите второе значение размера массива: '))
a = []
for i in range(n):
    a.append([int(m) for m in input().split()])
i = int(input())
j = int(input())
for f in range(n):
    a[f][i], a[f][j] = a[f][j], a[f][i]
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()

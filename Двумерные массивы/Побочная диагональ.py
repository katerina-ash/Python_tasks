# Задача «Побочная диагональ»
# Условие
# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
n = int(input('Введите число n, что бы получился массив n*n: '))
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i+j == n-1:
            a[i][j] = 1
        if i+j>=n:
            a[i][j] = 2
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
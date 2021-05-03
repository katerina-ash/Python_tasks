#Задача «Отрицательная степень»
#Условие
#Дано действительное положительное число a и целоe число n.
#Вычислите an. Решение оформите в виде функции power(a, n).
#Стандартной функцией возведения в степень пользоваться нельзя.
def power(a, n):
    square_a = 1
    for i in range(1, abs(n)+1):
        square_a *= a
    if n < 0:
        square_a = 1 / square_a
    return square_a
a = float(input())
n = int(input())
print("{:.6f}".format(power(a, n)))
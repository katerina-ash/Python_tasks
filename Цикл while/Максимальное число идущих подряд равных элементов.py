#Задача «Максимальное число идущих подряд равных элементов»
#Условие
#Дана последовательность натуральных чисел, завершающаяся числом 0.
#Определите, какое наибольшее число подряд идущих элементов
#этой последовательности равны друг другу.
b = int(input())
i = 1
c = 0
while b != 0:
    a = int(input())
    b, a = a, b
    if b == a:
        i += 1
    if i>c:
        c = i
    if b != a:
        i = 1
print(c)
#Задача «Гипотенуза»
#Условие
#Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
from math import sqrt
a = int( input() )
b = int( input() )
c = a**2 + b**2
c = sqrt(c)
print(c)

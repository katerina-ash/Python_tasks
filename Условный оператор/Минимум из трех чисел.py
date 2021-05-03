# Задача «Минимум из трех чисел»
# Условие
# Даны три целых числа. Выведите значение наименьшего из них.
a = int( input() )
b = int( input() )
c = int( input() )
if a<b:
    m = a
else:
    m = b
if c<m:
    print(c)
else:
    print(m)

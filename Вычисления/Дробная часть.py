# Задача «Дробная часть»
# Условие
# Дано положительное действительное число X. Выведите его дробную часть.
x = float( input() )
y = x % 1
print( "{:5.3f}".format(y) )

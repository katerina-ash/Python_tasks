# Задача «Первая цифра после точки»
# Условие
# Дано положительное действительное число X.
# Выведите его первую цифру после десятичной точки.
x = float( input() )
y = x % 1 // 0.1
y = int(y)
print(y)

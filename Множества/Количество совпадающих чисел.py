#Задача «Количество совпадающих чисел»
#Условие
#Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
#Примечание. Эту задачу на Питоне можно решить в одну строчку.))
a = set(input().split())
b = set(input().split())
print(len(a&b))
#Задача «Уникальные элементы»
#Условие
#Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
#Элементы нужно выводить в том порядке, в котором они встречаются в списке.
a = [int(s) for s in input().split()]
k = 0
for i in range(len(a)):
    for h in range(len(a)):
        if a[i] == a[h]:
            k += 1
    if k == 1:
        print(a[i], end=' ')
    k = 0
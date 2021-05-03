#Задача «Самое частое слово»
#Условие
#Дан текст: в первой строке задано число строк, далее идут сами строки.
#Выведите слово, которое в этом тексте встречается чаще всего.
#Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

max_coun = max(counter.values())

a=set()

for key in counter:
    if counter[key] == max_coun:
        a.add(key)

a = list(sorted(a))
print('Cлово, которое в этом тексте встречается чаще всего - ', a[0])
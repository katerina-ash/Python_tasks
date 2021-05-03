#Задача «Словарь синонимов»
#Условие
#Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом
#к парному ему слову. Все слова в словаре различны.

#Для слова из словаря, записанного в последней строке, определите его синоним.

dictionary = dict()

for i in range(int(input())):
    a = input().split()
    dictionary[a[0]] = a[1]

word = input()

for key in dictionary:
    if word == dictionary[key]:
        print(key)
    else:
        if word == key:
            print(dictionary[key])
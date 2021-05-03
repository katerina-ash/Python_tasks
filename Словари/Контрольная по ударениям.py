#Задача «Контрольная по ударениям»

#пустой словарь
dictionary = {}

#заполняем словарь ударений
for i in range(int(input())):
    s = input()
    base_form = s.lower() #переводим слово в нижний регистр
    if base_form not in dictionary:
        dictionary[base_form]=set() #если слова нет в словаре, то создается множество
    dictionary[base_form].add(s)
print(dictionary)

errors = 0 #число ошибок
petya = input().split() #ввод петиного предложения
for word in petya:
    base_form = word.lower()
    # если ключ(слово) есть в словаре и ударение не совпадают
    # или число заглавных букв не равно 1
    if (base_form in dictionary and word not in dictionary[base_form]
            or len([l for l in word if l.isupper()]) != 1):
        errors += 1
print(errors)
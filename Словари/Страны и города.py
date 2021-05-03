#Задача «Страны и города»
#Условие
#Дан список стран и городов каждой страны. Затем даны названия городов.
#Для каждого города укажите, в какой стране он находится.

# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# 3
# Odessa
# Moscow
# Novgorod

country_city = {}

for i in range(int(input())):
    line = input().split()
    country_city[line[0]] = tuple()
    for city in line[1:]:
        country_city[line[0]] = country_city[line[0]] + (city,)
print(country_city)

for i in range(int(input())):
    city = input()
    for key in country_city.keys():
        if city in country_city[key]:
            print(key)

#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Studio Silk
#
# Created:     12.12.2020
# Copyright:   (c) Studio Silk 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Задача «Потерянная карточка»
#Условие
#Для настольной игры используются карточки с номерами от 1 до N.
#Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
#Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N).
#Программа должна вывести номер потерянной карточки.

#Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.
N = int( input() )
sum1 = 0
for i in range(1, N+1):
    sum1 += i
for a in range (N-1):
    x = int( input() )
    sum1 -= x
print(sum1)
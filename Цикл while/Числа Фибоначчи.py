#Задача «Числа Фибоначчи»
#Условие
#Последовательность Фибоначчи определяется так:
#φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.

#По данному числу n определите n-е число Фибоначчи φn.

#Эту задачу можно решать и циклом for.
fib1 = 1
fib2 = 1
n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)
i = 0
if n == 0:
    print(0)
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
print(fib2)
# Даны целые положительные числа N и K. Используя только операции
# сложения и вычитания, найти частное от деления нацело N на K, а также
# остаток от этого деления.

n = int(input("Ввидите число N : "))  # Наше число, которое мы делим
k = int(input("Ввидите число K : "))
num = 0  # остаток от деления

while n >= k:
    n -= k  # n = n - k
    num = +1

print(n)
print(num)

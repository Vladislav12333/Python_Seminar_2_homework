# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def powers_of_two(N):
    power = 0
    while 2 ** power <= N:
        print(2 ** power)
        power += 1

N = int(input("Введите число N: "))
powers_of_two(N)


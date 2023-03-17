# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input("Ввидите число "))
i = 0
rezalt = 0
while i < number:
    rezalt = 2**i
    if rezalt > number:
        i = number  
    else:
        print(rezalt)
    i += 1
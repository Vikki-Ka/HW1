# Задача 2: Найдите сумму цифр трехзначного числа.

#  *Пример:*

#  123 -> 6 (1 + 2 + 3)
#  100 -> 1 (1 + 0 + 0) |

number = int(input("Ввидите трехзначное число: "))
digital1 = int(number / 100)
digital2 = int(number / 10 % 10)
digital3 = int(number % 10)

print(f"Сумма цыфр в числе {number} равна {digital1 + digital2 + digital3}")
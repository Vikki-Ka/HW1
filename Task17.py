# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.

from random import randint

#list =  [1, 1, 2, 0, -1, 3, 4, 4]
list_1 = []
#list_2 = set()
n = int(input("Ввидите число: "))
count = 0
for i in range(n):
    list_1.append(randint(1,10))
    #list_2.add(list_1[i])

#list_1 = [i for i in range(n)))] все ниже тоже самое
list_1 = [randint(1,10) for _ in range(int(input("Ввидите число: ")))]
list_1 = [int(input("ввидите число")) for _ in range(int(input("Ввидите число: ")))] #лист компликтейшен
print(list_1)
print(len(set(list_1)))

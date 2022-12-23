# Задайте список из нескольких чисел. Напишите программу, которая найдет сумму элементов списка, 
# которые стоят на нечетной позиции
'''
from random import randint
list = [randint(0,10) for i in range(randint(5,10))]
print(list)
summa = 0
for i in range(1,len(list),2):
    summa += list[i]
print(summa)
'''

# Напишите программу, которая найдет произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второой и предпоследний и т.д.
'''
from random import randint
list1 = [randint(0,10) for i in range(randint(5,10))]
print(list1)
list2 = []
a = len(list1)
b = a//2 +a%2
for i in range(b):
    list2.append(list1[i] * list1[a-i-1])
print(list2)
'''

# Задайте список из вещественных чисел. Напишите программу, которая найдет разницу между максимальным и
# минимальным значением дробной части элементов

import random
list1 = [round(random.uniform(0,10),2) for i in range(random.randint(5,10))]
print(list1)

def fract(num):
    return round(num%1,2)

list2 = list(map(fract,list1))
print(list2)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное


# Задайте число, составьте список чисел Фибоначчи, в том числе для отрицательных индексов


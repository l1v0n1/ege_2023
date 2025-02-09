'''
В магазине для упаковки подарков есть N кубических коробок. Самой интересной считается упаковка подарка по принципу
матрешки – подарок упаковывается в одну из коробок, та, в свою очередь, в другую коробку и т.д. Одну коробку можно
поместить в другую, если длина её стороны хотя бы на 3 единицы меньше длины стороны другой коробки. Определите
наибольшее количество коробок, которое можно использовать для упаковки одного подарка, и максимально возможную длину
стороны самой маленькой коробки, где будет находиться подарок. Размер подарка позволяет поместить его в самую маленькую коробку.
Входные данные представлены в файле 26-89.txt следующим образом. В первой строке входного файла записано число
N – количество коробок в магазине (натуральное число, не превышающее 10 000). В каждой из следующих N строк находится
значения длины стороны очередной коробки (натуральное число, не превышающее 10 000).
Запишите в ответе два целых числа: сначала наибольшее количество коробок, которое можно использовать для упаковки
одного подарка, затем максимально возможную длину стороны самой маленькой коробки в таком наборе.
'''
with open('../files/task26/26-89.txt') as f:
    n = int(f.readline())
    a = sorted([int(x) for x in f], reverse=True)
    k = 1
    box = a[0]
    for i in range(1, len(a)):
        if box - a[i] >= 3:
            k += 1
            box = a[i]
print(k, box)

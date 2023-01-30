'''
(А. Кабанов) В текстовом файле записан набор натуральных чисел. Гарантируется, что все числа различны.
Рассматриваются пары чисел с чётной суммой, такие что половина элементов последовательности больше, чем среднее
арифметическое элементов пары. Необходимо определить, сколько в наборе таких пар, и наибольшее из средних арифметических таких пар.
Входные данные представлены в файле 26-49.txt следующим образом. Первая строка содержит целое число
N – общее количество чисел в наборе. Каждая из следующих N строк содержит одно число, не превышающее 10**9.
В ответе запишите два целых числа: сначала количество пар, затем наибольшее среднее арифметическое.
'''
with open('../files/task26/26-49.txt') as f:
    n = int(f.readline())
    s = sorted([int(i) for i in f])
    ss = []
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if (s[i] + s[j]) % 2 == 0 and (s[i] + s[j]) / 2 < s[len(s) // 2]:
                ss.append((s[i] + s[j]) // 2)
print(len(ss), max(ss))


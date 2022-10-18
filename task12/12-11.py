'''
Дана программа для исполнителя Редактор:

НАЧАЛО
ПОКА нашлось (1111)
  заменить (1111, 2)
  заменить (22, 11)
КОНЕЦ ПОКА
КОНЕЦ
Известно, что исходная строка содержала более 100 единиц и не содержала других цифр.
Укажите минимально возможную длину исходной строки, при которой в результате работы этой программы получится строка,
содержащая минимально возможное количество единиц.

'''
minim = 100000
for i in range(101, 1000):
    s = i * '1'
    while '1111' in s:
        s = s.replace('1111', '2', 1)
        s = s.replace('22', '11', 1)
    if s.count('1') < minim:
        minim = s.count('1')
        min_i = i
print(min_i)

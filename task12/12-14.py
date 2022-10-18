'''
Дана программа для исполнителя Редактор:
НАЧАЛО
ПОКА нашлось(01) ИЛИ нашлось(02) ИЛИ нашлось(03)
  заменить(01, 2302)
  заменить(02, 10)
  заменить(03, 201)
КОНЕЦ ПОКА
КОНЕЦ
Известно, что исходная строка начиналась с нуля, а далее содержала только единицы, двойки и тройки.
После выполнения данной программы получилась строка, содержащая 60 единиц, 22 двойки и 17 троек. Сколько единиц было в исходной строке?
'''
for a in range(1, 50):
    for b in range(1, 50):
        for c in range(1, 50):
            s = '0' + a * '1' + b * '2' + c * '3'
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)
            if s.count('1') == 60 and s.count('2') == 22 and s.count('3') == 17:
                print(a)
                break

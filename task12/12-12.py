'''
(А.А. Имаев) Дана программа для исполнителя Редактор:
НАЧАЛО
ПОКА нашлось (12) ИЛИ нашлось (1)
  ЕСЛИ нашлось (12)
    ТО заменить (12, 2221)
    ИНАЧЕ заменить (1,222222)
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей одной единицы и 51 стоящих справа от неё цифр 2? В ответ, запишите, сколько цифр 2 будет в конечной строке.
'''
s = '1' + 51 * '2'
while '12' in s or '1' in s:
    if '12' in s:
        s = s.replace('12', '2221', 1)
    else:
        s = s.replace('1', '222222', 1)
print(s.count('2'))

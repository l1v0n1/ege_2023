'''
(А. Комков) Исполнитель Нолик преобразует число, записанное на экране в четверичной системе счисления. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 2
2. Прибавить 3
3. Добавить справа 0
Первая команда увеличивает число на 2. Вторая команда увеличивает число на 3. Третья команда приписывает к записи числа справа 0,
например, для числа 123 результатом работы данной команды будет являться число 1230.
Сколько существует программ, которые число 1, записанное в четверичной системе счисления, преобразуют в четверичную запись 100?
'''
def chet(a):
    s = ''
    while a > 0:
        s = str(a % 4) + s
        a //= 4
    return s

def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 2, y) + f(x + 3, y) + f(int(chet(x) + '0', 4), y)


print((f(1, int('100', 4))))
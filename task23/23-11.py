'''
Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 2
3. Умножить на 3
Программа для исполнителя Калькулятор – это последовательность команд. Сколько существует программ,
для которых при исходном числе 2 результатом является число 15, и при этом траектория вычислений содержит числа 4 и 11?
'''
def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)


print(f(2, 4) * f(4, 11) * f(11, 15))
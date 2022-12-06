'''
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит две кучи камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в любую кучу один камень или добавить добавить в любую кучу столько камней, сколько их в данный момент в другой куче. Игра завершается в тот момент, когда общее количество камней в двух кучах становится не менее 58. Победителем считается игрок, сделавший последний ход. В начальный момент в первой куче было 6 камней, а во второй – S камней, 1 ≤ S ≤ 51.
Ответьте на следующие вопросы:
  Вопрос 1. Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Назовите минимальное значение S, при котором это возможно.
  Вопрос 2. Найдите минимальное и максимальное значение S, при котором у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.
  Вопрос 3. Найдите значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
'''
#19
def f(x, p):
    if x >= 58 and p == 2:
        return True
    else:
        if x < 58 and p == 2:
            return False
    return f(x + 1, p + 1) or f(x * 2, p + 1)


print(min([i for i in range(1, 52) if f(6, i, 0)]))
#20
def f(x, y, p):
    if x + y >= 58 or p > 3:
        return p == 3
    if p % 2:
        return f(x + 1, y, p + 1) and f(x + y, y, p + 1) and \
               f(x, y + 1, p + 1) and f(x, x + y, p + 1)
    else:
        return f(x + 1, y, p + 1) or f(x + y, y, p + 1) or \
        f(x, y + 1, p + 1) or f(x, x + y, p + 1)


print([i for i in range(1, 52) if f(6, i, 0)])
#21
def f(x, y, p):
    if x + y >= 58 and (p == 2 or p == 4):
        return True
    else:
        if x + y < 58 and p == 4:
            return False
        else:
            if x + y >= 58:
                return False
    if p % 2 == 0:
        return f(x + 1, y, p + 1) and f(x + y, y, p + 1) and \
               f(x, y + 1, p + 1) and f(x, x + y, p + 1)
    else:
        return f(x + 1, y, p + 1) or f(x + y, y, p + 1) or \
        f(x, y + 1, p + 1) or f(x, x + y, p + 1)


print(min([i for i in range(1, 52) if f(6, i, 0)]))
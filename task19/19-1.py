'''
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в одну из куч один камень, увеличить количество камней в первой куче в два раза или увеличить количество камней во второй куче в три раза. Например, пусть в одной куче 6 камней, а в другой 9 камней; такую позицию мы будем обозначать (6, 9). За один ход из позиции (6, 9) можно получить любую из четырёх позиций: (7, 9), (12, 9), (6, 10), (6, 27). Чтобы делать

ходы, у каждого игрока есть неограниченное количество камней.

Игра завершается в тот момент, когда суммарное количество камней в кучах становится не менее 84. Победителем считается игрок, сделавший последний ход, то есть первым получивший позицию, в которой в кучах будет 84 или больше камней.

В начальный момент в первой куче было 16 камней, во второй куче  — S камней, 1 ≤ S ≤ 67.

Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника. Описать стратегию игрока  — значит, описать, какой ход он должен сделать в любой ситуации, которая ему может встретиться при различной игре противника. В описание выигрышной стратегии не следует включать ходы играющего по ней игрока, которые не являются для него безусловно выигрышными, т.е не гарантирующие выигрыш независимо от игры противника.

Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Укажите минимальное значение S, когда такая ситуация возможна.
'''


def f(x, y, h):
    if h == 3 and x + y >= 84:
        return 1
    elif h == 3 and x + y < 84:
        return 0
    elif x + y >= 84 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1) or f(x * 3, y, h + 1)  # стратегия победителя
        else:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1) or f(x * 3, y, h + 1)  # стратегия проигравшего(неудачный ход)
 
for x in range(1, 68):
    if f(x, 16, 1) == 1:
        print("Задача 19:", x)
        break
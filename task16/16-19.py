'''
Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:

F(n) = n, при n ≤ 5,
F(n) = n + F(n/2 – 3), когда n > 5 и делится на 8,
F(n) = n + F(n + 4) , когда n > 5 и не делится на 8.
Назовите максимальное значение n, для которого возможно вычислить F(n).

'''
def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 8 == 0:
        return n + f(n/2 - 3)
    if n > 5 and n % 8 != 0:
        return n + f(n + 4)

for n in range(1, 1000):
    try:
        f(n)
        print(n)
    except BaseException:
        pass

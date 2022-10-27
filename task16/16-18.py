'''
Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:

F(n) = n, при n ≤ 1,
F(n) = n + F(n/3 – 1), когда n > 1 и делится на 3,
F(n) = n + F(n + 3) , когда n > 1 и не делится на 3.
Назовите минимальное значение n, для которого F(n) определено и больше 1000.

'''
def f(n):
    if n <= 1:
        return n
    else:
        if n % 3 == 0:
            return n + f(n / 3 - 1)
        else:
            return n + f(n + 3)

for n in range(1, 10000):
    try:
        if f(n) > 1000:
            print(n)
            break
    except BaseException:
        pass

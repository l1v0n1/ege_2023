'''
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

F(n) = 5–n при n < 5
F(n) = 4·(n – 5)·F(n–5), если n ≥ 5 и делится на 3,
F(n) = 3·n + 2·F(n–1) + F(n–2), если n ≥ 5 и не делится на 3.
Чему равно значение функции F(20)?

'''
def f(n):
    if n < 5:
        return 5 - n
    else:
        if n % 3 == 0:
            return 4 * (n - 5) * f(n - 5)
        else:
            return 3 * n + 2 * f(n - 1) + f(n - 2)


print(f(20))
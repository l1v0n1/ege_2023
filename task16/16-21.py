'''
Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:

F(n) = 1, при n < 2,
F(n) = F(n/3) + 1, когда n ≥ 2 и делится на 3,
F(n) = F(n - 2) + 5, когда n ≥ 2 и не делится на 3.
Назовите количество значений n на отрезке [1;100000], для которых F(n) равно 55.

'''
s = 100000 * [1]
for n in range(len(s)):
    if n >= 2:
        if n % 3 == 0:
            s[n] = s[n // 3] + 1
        else:
            s[n] = s[n - 2] + 5

print(s.count(55))

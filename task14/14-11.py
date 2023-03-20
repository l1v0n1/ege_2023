'''
Значение выражения 81**79 + 75**2022 – 12**35 записали в системе счисления с основанием 5. Определите количество комбинаций цифр 4# в этой записи, где # – любая цифра от 1 до 3.
'''
x = 81 ** 79 + 75 ** 2022 - 12 ** 35
s = ''
k = 0
while x:
    s = str(x % 5) + s
    x //= 5
for i in range(len(s)-1):
    if s[i] == '4' and s[i + 1] in '123':
        k += 1
print(k)
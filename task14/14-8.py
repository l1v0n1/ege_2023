'''
(М.В. Кузнецова) Значение арифметического выражения: 9**7 + 3**21 – 8 записали в системе счисления с основанием 3. Найдите сумму цифр в этой записи. Ответ запишите в десятичной системе
'''
summa = 0
x = 9 ** 7 + 3 ** 21 - 8
while x:
    summa += x % 3
    x //= 3
print(summa)
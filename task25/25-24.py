'''
Обозначим через P(N) – произведение 5 наименьших различных нетривиальных делителей натурального числа N (не считая единицы и самого числа).
Если у числа N меньше 5 таких делителей, то P(N) считается равным нулю. Найдите 5 наименьших натуральных чисел,
превышающих 400 000 000, для которых P(N) оканчивается на 17 и не превышает N. В ответе для каждого найденного числа
запишите сначала значение P(N), а затем – наибольший делитель, вошедший в произведение P(N).
'''
i = 400000001
k = 0
while k != 5:
    divs = set()
    for d in range(2, round(i ** 0.5)+1):
        if i % d == 0:
            divs.add(d)
            divs.add(i // d)
    divs = sorted(divs)
    if len(divs) >= 5:
        p = divs[0] * divs[1] * divs[2] * divs[3] * divs[4]
        if p <= i and p % 100 == 17:
            k += 1
            print(p, divs[4])
    i += 1

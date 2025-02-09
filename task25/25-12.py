'''
Рассматриваются целые числа, принадлежащих числовому отрезку [238941; 315675], которые представляют собой произведение
двух различных простых делителей. В ответе запишите количество таких чисел и такое из них, простые делители которого
отличаются друг от друга больше всего. Если чисел с наибольшей разностью делителей несколько, запишите в ответе наименьшее из них.
'''
def prost(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


mx = 0
count = 0
for i in range(238941, 315676):
    for d in range(2, round(i ** 0.5)):
        if d * (i // d) == i and prost(d) and prost(i // d):
            count += 1
            if abs(i // d - d) > mx:
                mx = abs(i // d - d)
                d1 = i
print(count, d1)

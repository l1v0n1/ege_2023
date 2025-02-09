'''
В файле 17-1.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения
от –10 000 до 10 000 включительно. Определите количество троек, в которых хотя бы два из трёх элементов меньше,
чем среднее арифметическое всех чисел в файле, и десятичная запись хотя бы двух из трёх элементов содержит цифру 5.
В ответе запишите два числа: сначала количество найденных троек, а затем – максимальную сумму элементов таких троек.
В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
'''
def nCond(a, fun):
  return [fun(k) for k in a].count(True)

with open('../files/task17/17-1.txt') as f:
    s = [int(x) for x in f]
    sred = sum(s) / len(s)
    res = []
    for i in range(len(s) - 2):
        triple = s[i:i+3]
        if nCond(triple, lambda x: x < sred) >= 2 and nCond(triple, lambda x: '5' in str(x)) >= 2:
            res.append(sum(triple))
print(len(res), max(res))

'''
В файле 17-4.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения
от 0 до 10 000 включительно. Определите количество пар, в которых хотя бы один из двух элементов больше,
чем среднее арифметическое всех чисел в файле, а их сумма оканчивается на 9. В ответе запишите два числа:
сначала количество найденных пар, а затем – минимальную сумму элементов таких пар.
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
with open('../files/task17/17-4.txt') as f:
    s = [int(x) for x in f]
    numbers = []
    sred = sum(s) /  len(s)
    for i in range(len(s) - 1):
        if (s[i] + s[i + 1]) % 10 == 9 and (s[i] > sred or s[i + 1] > sred):
            numbers.append(s[i] + s[i + 1])
print(len(numbers), min(numbers))

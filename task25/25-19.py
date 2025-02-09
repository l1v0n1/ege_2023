'''
Найдите все натуральные числа, N, принадлежащие отрезку [100 000 000; 300 000 000], которые можно представить в виде
N = 2m•7n, где m – нечётное число, n – чётное число. В ответе запишите все найденные числа в порядке возрастания, а справа от каждого числа – сумму m+n.
'''
ans = []
for m in range(1, 1000, 2):
    for n in range(0, 1000, 2):
        if 100000000 <= 2 ** m * 7 ** n <= 300000000:
            ans.append((2 ** m * 7 ** n, m + n))
print(sorted(ans))
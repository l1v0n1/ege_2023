'''
Сколько значащих нулей в двоичной записи числа

  4**512 + 8**512 – 2**128 – 250

'''
print(bin(4 ** 512 + 8 ** 512 - 2 ** 128 - 250).count('0') - 1)
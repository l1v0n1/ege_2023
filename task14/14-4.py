'''
Сколько значащих нулей в двоичной записи числа

  4 ** 812 + 8 ** 800 - 2 ** 3125 - 8 ** 65 - 4 ** 312 + 130

'''
print(bin(4 ** 812 + 8 ** 800 - 2 ** 3125 - 8 ** 65 - 4 ** 312 + 130).count('0') - 1)
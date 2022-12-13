'''
Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавь 1
2. Прибавь 3
3. Умножь на 2
Первая команда увеличивает число на экране на 1, вторая увеличивает его на 3, третья – умножает на 2.
Программа для исполнителя – это последовательность команд. Сколько существует программ, которые преобразуют
исходное число 2 в число 51, и при этом траектория вычислений содержит число 18 и не содержит число 33. Также программа не должна содержать двух команд «Умножь на 2» подряд.
'''
from functools import lru_cache

@lru_cache
def f( start, end, lastCmd ):
  if start == end: return 1
  if start == 33 or start > end: return 0
  count =  f( start+1, end, 1 )
  count += f( start+3, end, 2 ) if start not in [16,17] else 0
  count += f( start*2, end, 3 ) if lastCmd != 3 and not(10<=start<=17) else 0
  return count

print( f( 2, 51, 0 ) )
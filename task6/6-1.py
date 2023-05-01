
import turtle as t  # Подключим модуль черепашка
x1 = t.xcor()#Получить x координату черепашки
y1 = t.ycor()#Получить y координату черепашки
t.speed(10)
for i in range(9):  # пропишем алгоритм построения фигуры по условию
    t.forward(18)
    t.right(72)
x2 = t.xcor()
y2 = t.ycor()
print(round(((x2 - x1)**2 + (y2 - y1)**2))**0.5)
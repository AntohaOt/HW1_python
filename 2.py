x = int(input())
y = int(input())
x2 = int(input())
y2 = int(input())

position1 = 4
position2 = 4

# Определим четверть у первой точки:
if x > 0 and y > 0:
    position1 = 1

elif x < 0 and y > 0:
    position1 = 2

elif x < 0 and y < 0:
    position1 = 3


# Определим четверть у второй точки:
if x2 > 0 and y2 > 0:
    position2 = 1

elif x2 < 0 and y2 > 0:
    position2 = 2

elif x2 < 0 and y2 < 0:
    position2 = 3


# Выполняем проверку условия, и если четверти одинаковые - выводим результат "YES" в консоль; если четверти разные - "NO":
if position1 == position2:
    print("YES")
else:
    print("NO")
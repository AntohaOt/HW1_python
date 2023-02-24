a = int(input())
b = int(input())

# Проверка на бесконечное количество решений:
if a == 0 and b == 0:
    print("INF")

# Проверка с помощью выражения, которое дано в условии задачи:
elif a * int(-b / a) + b != 0:
    print("NO")
else:
    print(int(-b / a))
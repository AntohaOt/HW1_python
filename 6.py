a = int(input())
b = int(input())
c = int(input())

# Вычисление с помощью формулы дискриминанта: 
discriminant = b**2 - 4 * a * c

# Проверка на отрицательный дискриминант:
if discriminant < 0:
    print("Решений нет!")

else:
    # Вычисление 1 и 2 корней по формулам:
    x1 = int(-b - discriminant**0.5 / (2 * a))
    x2 = int(-b + discriminant**0.5 // (2 * a))

    # Проверка на одинаковые корни:
    if x1 == x2:
        print(x1)
    else:
        print(x1)
        print(x2)
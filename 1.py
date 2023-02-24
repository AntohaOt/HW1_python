k = int(input())
m = int(input())
n = int(input())

# То, сколько раз нам нужно будет пожрить одну сторону у всех имеющихся котлет:
n * 2 // k

# Проверка на четность сторон; проверка на максимальное колличество котлет на сковороде:
if n * 2 % k == 0:
    res = m * (n * 2 // k)

# Проверка, что количество котлет будет меньше (либо равно колличеству котлет), которое помещается на сковородке:
elif n <= k:
    # Результатом является время, затраченное на одновременное обжаривание котлет с обеих сторон:
    res = m * 2

else:
    # Логика с лишним подходом:
    res = m * ((n * 2 // k) + 1)

print(res)

# Количество коров
number = input()

# Проверим, на что оканчивается последний элемент строки: на 0, или он находится в промежутках от "5 до 10" и от "11 до 20" включительно:
if number[-1] == "0" or 5 <= int(number[-1]) <= 10 or 11 <= int(number[-2:]) <= 20:
    print(number + " korov") 

# Проверим, оканчивается ли строка на 1:
elif number[-1] == "1":
    print(number + " korova")

else:
    print(number + " korovy")
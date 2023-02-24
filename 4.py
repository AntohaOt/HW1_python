num = input()

units = " "
dozens = " "

# Формируем единицы:
if num[-1] == "1":
    units = "I"
elif num[-1] == "2":
    units = "II" 
elif num[-1] == "3":
    units = "III"
elif num[-1] == "4":
    units = "IV"
elif num[-1] == "5":
    units = "V"
elif num[-1] == "6":
    units = "VI"
elif num[-1] == "7":
    units = "VII"
elif num[-1] == "8":
    units = "VIII"
elif num[-1] == "9":
    units = "IX"

# Формируем десятки:
if int(num) > 9:
    if int(num[0]) == 4:
        dozens = "XL"
    elif 9 > int(num[0]) >= 5:
        dozens = "L" + "X" * (int(num[0]) - 5)
    elif int(num[0]) == 9:
        dozens = "XM"
    elif int(num) == 100:
        dozens = "M"
    else:
        dozens = "X" * int(num[0])

print(dozens + units)
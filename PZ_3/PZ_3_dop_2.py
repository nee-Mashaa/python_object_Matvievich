# Ввести двухзначное число. Если оно четное, разделить на 4, если нечетное - умножить на 5.
a = input("Введите число: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Ошибка: ввели число не верно!")
        a = input("Введите число: ")
if a % 2 == 0:
    a *= 4
    print(a)
else:
    a *= 5
    print(a)

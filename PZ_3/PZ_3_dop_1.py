# Ввести 2 число. Если их произведение отрицательно, умножить его на 8, в противном случае увеличить его в 1.5 раза
a, b = input("Введите первое число: "), input("Введите второе число: ")
while type(a) != int and type(b) != int:
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Ошибка: неправильно ввели число!")
        a, b = input("Введите первое число: "), input("Введите второе число: ")
mod = a * b
if mod < 0:
    mod *= 8
    print(mod)
else:
    mod *= 1.5
    print(mod)
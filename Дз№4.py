# Задача №4: Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

i = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))

x = ""

while i != 0:
    x = str(i % 2) + x
    i //= 2

print(x)

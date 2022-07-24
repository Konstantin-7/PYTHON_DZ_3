# Задача №2: Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#	[2, 3, 4, 5, 6] => [12, 15, 16];
#	[2, 3, 5, 6] => [12, 15]


def the_product_of_pairs_of_list_numbers(listt):
    if len(listt) % 2 != 0:
        l = len(listt)//2 + 1
    else:
        l = len(listt)//2
    for i in range(l):
        new_lst = listt[i]*listt[len(listt)-i-1]
        print(new_lst)


listt = list(map(int, input("Введите числа через пробел:\n").split()))
the_product_of_pairs_of_list_numbers(listt)

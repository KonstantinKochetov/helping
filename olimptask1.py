# coding=utf-8
# если число четное то всегда пополам
# если нечетное то делим пополам и идем вниз до первого делителя, а потом вычитаем этот делитель из исходного числа
# 124: просто делим пополам: 62 62
# 125: делим на 2 получаем 62, идем вниз до первого делителя получаем 25, а потом вычитаем 25 из 125 -> получаем 25 и 100

user_input = int(input())

first = 0
second = 0

if (user_input % 2 == 0):
    first = user_input / 2
    second = first
else:
    first = user_input / 2
    while (user_input % first) != 0:
        first -= 1
    second = user_input - first

print(str(first) + ' ' + str(second))

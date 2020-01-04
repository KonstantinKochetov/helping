# coding=utf-8
# карта сокровищ
# списки нельзя использовать ибо это очень долго, программа не выполняется за 1 сек
# используем словари
# каждую строку обрабатываем следующим образом:
# 1. сохраняем строки x и y кроме последнего значения как один ключ в словаре
# 2. В значении по этому ключу указываем сначала 1 потом если опять этот ключ попадается то увеличиваем на 1
# 3. Выбираем наибольшее значение

dictionary = dict()
new_max = 1
current_max = 1

user_input = int(input())
for i in range(user_input):
    line = input().split()

    key_x = line[0][:-1]
    key_y = line[1][:-1]
    key = key_x + key_y
    if key in dictionary:
        new_max = dictionary[key] + 1
        dictionary[key] = new_max
    else:
        new_max = 1
        dictionary[key] = new_max

    if new_max >= current_max:
        current_max = new_max

print(current_max)



# coding=utf-8
# симметризовать таблицу
# сохраняем пути в словаре (01: 3, 10: 3, 02: 6, 20:6, 12:1, 21:1...)
# выводим на экран

dictionary = dict()
user_input = int(input())
for index in range(user_input - 1):
    line = input().split()
    for i, price in enumerate(line):
        way = str(i) + str(index + 1)
        back_way = str(index + 1) + str(i)
        dictionary[way] = price
        dictionary[back_way] = price

for index in range(user_input):
    output_string = ''
    for jindex in range(user_input):
        if index == jindex:
            output_string = output_string.strip() + ' ' + str(0)
        else:
            output_string = output_string.strip() + ' ' + dictionary[str(index) + str(jindex)]
    print(output_string)

# coding=utf-8
# проверка связи
# сохраняем слова в словарь как ключи
# если ключ уже присутствует то увеличиваем счетчик на 1 (для каждого слова свой счетчик)
dictionary = dict()

output_string = ''
user_input = input().split()
for key in user_input:
    if key in dictionary:
        maximum = dictionary[key] + 1
        dictionary[key] = maximum
    else:
        maximum = 1
        dictionary[key] = maximum

    output_string = output_string.strip() + ' ' + str(maximum)
print(output_string)


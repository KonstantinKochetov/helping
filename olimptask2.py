# coding=utf-8
# когда 1 путь увеличиваем только y, когда 2 путь увеличиваем x и y ....

user_input = int(input())
x = 0
y = 0

# TODO: можно улучшить словарями. Положить функцию в значение и просто вызывать функцию, увеличивающие x или y
for i in range(user_input):
    line = input().split()
    direction = int(line[0])
    increase = int(line[1])
    if direction == 1:
        y += increase
    elif direction == 2:
        y += increase
        x += increase
    elif direction == 3:
        x += increase
    elif direction == 4:
        y -= increase
        x += increase
    elif direction == 5:
        y -= increase
    elif direction == 6:
        y -= increase
        x -= increase
    elif direction == 7:
        x -= increase
    elif direction == 8:
        y += increase
        x -= increase

# TODO: сделать получше
print(str(x) + '.000' + ' ' + str(y) + '.000')
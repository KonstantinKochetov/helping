# coding=utf-8
# берем два первых числа и печатаем их пока значение любого не дойдет до 0. Когда дошло берем следующее число

_ = int(input())
temp_user_input = input().split()
user_input = map(lambda x: int(x), temp_user_input)

# user_input = [5, 2, 7, 1]
# 6
# 1 2
# 1 2
# 1 3
# 1 3
# 1 3
# 3 4

# user_input = [1, 2, 1, 1]
# 2
# 1 2
# 2 3

counter = 0
output_string = ''
max_len = len(user_input)
left_index = 0
right_index = 1

left_counter = user_input[left_index]
right_counter = user_input[right_index]

while left_counter != 0 and right_counter != 0:
    counter += 1
    left_counter -= 1
    right_counter -= 1
    middle_char = ''
    if output_string:
        middle_char = '\n'
    else:
        middle_char = ''
    output_string = output_string + middle_char + str(left_index + 1) + ' ' + str(right_index + 1)
    if left_counter == 0:
        left_index = (max(left_index, right_index) + 1)
        if left_index < max_len:
            left_counter = user_input[left_index]
            current_left_value = user_input[left_index]
        # swap everything
        left_index, right_index, left_counter, right_counter = right_index, left_index, right_counter, left_counter
    if right_counter == 0:
        right_index = (max(left_index, right_index) + 1)
        if right_index < max_len:
            right_counter = user_input[right_index]

print(counter)
print(output_string)

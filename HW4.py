input_parameter = input('Введите данные:')

if input_parameter.isdigit():
    print(input_parameter[::-1])
else:
    print('Введите число')
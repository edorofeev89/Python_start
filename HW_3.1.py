input_parameter = input('Введите данные:')

result_1 = f'Это строка в которую {input_parameter} новую строку'
result_2 = result_1.replace(input_parameter, 'замена в строке')

print(result_1)
print(result_2)
print(len(result_1))

if result_1.find('строка'):
    print('Да')
else:
    print('НЕТ')

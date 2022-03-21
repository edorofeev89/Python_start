input_parameter = int(input('Введите число:'))
result = 0

while input_parameter != 0:
    numb = input_parameter % 10
    input_parameter = input_parameter // 10

    result = result * 10 + numb

print(result)
a = int(input("Введите высоту фигуры в символах:"))

for i in range(a):
    print(('  ' * (a - i)) + (i * ' *') + ' * ' + (i * '* '))

for i in reversed(range(a - 1)):
    if i != 0:
        r = (i - 1) * '  ' + ' * ' + (i - 1) * '  ' + '* '
    else:
        r = ''
    print(('  ' * (a - i)) + ' *' + r)
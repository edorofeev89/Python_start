def square(number):
    return number * 4, number ** 2, 2 ** 0.5 * number


if __name__ == '__main__':

    result = square(int(input("Введите сторону квадрата:")))
    print(f"Периметр: {result[0]}\n"
          f"Площадь: {result[1]}\n"
          f"Диагональ: {result[2]}")
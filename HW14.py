def multiplication(n):
    result = 1
    for i in str(n):
        if int(i) != 0:
            result = int(i) * result
        else:
            result
    return result

if __name__ == '__main__':

    number = int(input("Введите число:"))

print(f"Итог: {multiplication(number)}")
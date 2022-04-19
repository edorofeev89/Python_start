def arithmetic(a, b, symbol):
    action = {"+": a + b, "-": a - b, "*": a * b, "/": a / b}
    return action.get(symbol, "Неизвестная операция.")

if __name__ == '__main__':
    result = arithmetic(int(input("Первое число:")),
                        int(input("Второе число:")),
                        input("Математический символ:"))

    print (f"Итого: {result}")

def generator_function(n):
    for i in range(1, n + 1):
        yield i ** 2

def main():
    # Ввод числа N от пользователя
    N = int(input("Введите число N: "))

    # Использование функции-генератора
    print("Использование функции-генератора:")
    for square in generator_function(N):
        print(square)

    # Использование генераторного выражения
    print("\nИспользование генераторного выражения:")
    for square in (i ** 2 for i in range(1, N + 1)):
        print(square)

if __name__ == "__main__":
    main()

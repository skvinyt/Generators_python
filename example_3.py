def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_sequence = [0, 1]
    for _ in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence

# Пример использования функции
n = int(input("Введите число n: "))
print(f"Первые {n} чисел Фибоначчи:")
for number in fibonacci(n):
    print(number)

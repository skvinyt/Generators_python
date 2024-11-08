def substrings(s):
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield s[start:end]

# Пример использования функции
s = "abcsdfjjvndfu"
print("Все возможные подстроки:")
for substring in substrings(s):
    print(substring)

# Входные данные
names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["7%", "5%", "19%"]

# Однострочный генератор словаря
result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}

# Вывод результата
print(result)

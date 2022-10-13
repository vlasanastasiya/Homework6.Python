# Написать программу используz LIST Comprehension по поиску макс и мин числа

numbers = [int(i) for i in input("Введите числа: ").split()]
print(numbers)
print(f'{max(numbers)} {min(numbers)}')
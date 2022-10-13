#Найти корни квадратного уравнения Ax ** 2 + bx + c = 0. Используя MAP

a, b, c = list(map(int, input("Введите три числа: ").split()))
d = b ** 2 - 4 * a * c
if d > 0: print((-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a))
elif d == 0: print(- b/ (2 * a))
else: print("корней нет")



#Написать программу которая поместит элементы списка, стоящие на нечетных позициях в новый используя 
# Enumerate

List = [3, 10, 58, 73, 8, 5, 2]
numbers_1 = [y for x,y in enumerate(List) if x%2 != 0]
numbers_2 = [y for x,y in enumerate(List) if x%2 == 0]
print(numbers_2)
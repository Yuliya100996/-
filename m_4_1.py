from module_4_practic import *

data_1 = list(map(int, input('Введите число через пробел ').split()))
data_2 = list(map(int, input('Введите число через пробел ').split()))

bubble_sort(data_1)
selection_sort(data_2)

print('Пузырьковая сортировка:', data_1)
print('Сортировка выбором:', data_2)


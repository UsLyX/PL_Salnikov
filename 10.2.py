import numpy as np

def sort_columns_by_kth_row(matrix, k):
    k -= 1  # Преобразование к нулевой индексации
    kth_row = matrix[k]  # Получение k-й строки
    sorted_indices = np.argsort(kth_row)  # Индексы сортировки
    sorted_matrix = matrix[:, sorted_indices]  # Перестановка столбцов
    return sorted_matrix

# Чтение матрицы и параметра k из файла
def read_matrix_and_k_from_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        k = int(lines[0])  # Первое число — это значение k
        matrix = np.array([list(map(int, line.split())) for line in lines[1:]])
    return matrix, k

# Запись результирующей матрицы в файл
def write_matrix_to_file(output_file, matrix):
    with open(output_file, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

# Основная программа
input_file = 'Сальников_У-244_vvod.txt'
output_file = 'Сальников_У-244_vivod.txt'

# Чтение данных, обработка и запись результата
matrix, k = read_matrix_and_k_from_file(input_file)
sorted_matrix = sort_columns_by_kth_row(matrix, k)
write_matrix_to_file(output_file, sorted_matrix)

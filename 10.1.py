def is_sorted_ascending(row):
    return all(row[i] <= row[i + 1] for i in range(len(row) - 1))

def is_sorted_descending(row):
    return all(row[i] >= row[i + 1] for i in range(len(row) - 1))

def max_from_sorted_rows(matrix):
    max_element = None
    
    for row in matrix:
        if is_sorted_ascending(row) or is_sorted_descending(row):
            row_max = max(row)
            if max_element is None or row_max > max_element:
                max_element = row_max
                
    return max_element

# Чтение матрицы из файла
def read_matrix_from_file(input_file):
    with open(input_file, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

# Запись результата в файл
def write_result_to_file(output_file, result):
    with open(output_file, 'w') as file:
        file.write(str(result))

# Основная программа
input_file = 'Сальников_У-244_vvod.txt'
output_file = 'Сальников_У-244_vivod.txt'

# Чтение данных, обработка и запись результата
matrix = read_matrix_from_file(input_file)
result = max_from_sorted_rows(matrix)
write_result_to_file(output_file, result)

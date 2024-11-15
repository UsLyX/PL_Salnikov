import numpy as np

def sort_columns_by_kth_row(matrix, k):
    
    k -= 1
    
    
    kth_row = matrix[k]
    
    
    sorted_indices = np.argsort(kth_row)
    
    
    sorted_matrix = matrix[:, sorted_indices]
    
    return sorted_matrix


M = 4  # Число строк
N = 5  # Число столбцов
matrix = np.array([
    [5, 2, 9, 3, 8],
    [1, 7, 4, 6, 3],
    [3, 8, 2, 5, 7],
    [9, 4, 6, 1, 0]
])

k = 2  


sorted_matrix = sort_columns_by_kth_row(matrix, k)


print("Исходная матрица:")
print(matrix)
print(f"\nМатрица после сортировки столбцов по {k}-й строке:")
print(sorted_matrix)

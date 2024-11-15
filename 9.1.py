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


matrix = [
    [1, 2, 3],  # Упорядочено по возрастанию
    [5, 4, 3],  # Упорядочено по убыванию
    [7, 8, 9],  # Упорядочено по возрастанию
    [10, 20, 15]  # Неупорядочено
]


result = max_from_sorted_rows(matrix)
print(result)

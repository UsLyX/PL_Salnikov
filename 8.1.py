def count_numbers(a, b, c, N):
    
    digits = {str(a), str(b), str(c)}
    
    
    count = 0
    
    
    for num in range(100, N + 1):
        
        num_str = str(num)
        
        
        if all(digit in digits for digit in num_str):
            count += 1
    
    return count


a = int(input()) 
b = int(input())  
c = int(input())  
N = 210  

result = count_numbers(a, b, c, N)
print(result)
def reverse_words_in_string(s):
    
    words = s.split()
    
    
    words.reverse()
    
    
    reversed_s = ' '.join(words)
    
    return reversed_s


input_string = input()
output_string = reverse_words_in_string(input_string)
print(output_string)
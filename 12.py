# Блок А
print("Блок А")
def reverse_number(n):
    if n < 10:
        print(n, end="")
    else:
        print(n % 10, end="")
        reverse_number(n // 10)

number = 12345
reverse_number(number)

# Блок Б
print("\nБлок Б")
def find_two_largest(seq, first_max=0, second_max=0):
    if seq == 0:
        return second_max
    if seq > first_max:
        return find_two_largest(int(input()), seq, first_max)
    elif seq > second_max:
        return find_two_largest(int(input()), first_max, seq)
    return find_two_largest(int(input()), first_max, second_max)

print("Введите последовательность чисел, заканчивающуюся 0:")
result = find_two_largest(int(input()))
print("Второе по величине число:", result)
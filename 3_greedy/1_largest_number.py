# you've been asked to arrange a digits of a number in a row such that you get the largest possible number

def largest_number(num_array):
    largest = []
    while len(num_array) > 0:
        x = max(num_array)
        num_array.remove(x)
        largest.append(x)
    return largest


print(largest_number([1, 3, 6, 3, 9, 2, 7])) #prints [9, 7, 6, 3, 3, 2, 1]
print(largest_number([465, 46, 427, 4, 42]))
def selection_sort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                A[j], A[min_index] = A[min_index], A[j]
    return A


print(selection_sort([12, 3, 5, 8, 9, 17])) 
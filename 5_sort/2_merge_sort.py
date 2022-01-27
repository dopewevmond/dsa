from math import ceil

def merger(A, B):
    merged = []
    while len(A) > 0 and len(B) > 0:
        a = A[0]
        b = B[0]
        if b <= a:
            merged.append(b)
            B.pop(0)
        else:
            merged.append(a)
            A.pop(0)
    if len(A) > 0:
        merged.extend(A)
    else:
        merged.extend(B)
    return merged

def merge_sort(A):
    if len(A) <= 1:
        return A
    midpoint = (ceil(len(A)/2))
    B = merge_sort(A[:midpoint])
    C = merge_sort(A[midpoint:])
    sorted_A = merger(B, C)
    return list(sorted_A)

print(merge_sort([12, 3, 5, 8, 9, 7]))
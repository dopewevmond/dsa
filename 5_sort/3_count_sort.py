def count_sort(A, M):
    """ 
        this is a non comparison based sorting algorithm \n
        this implementation works for only numbers \n
        the range of numbers to be sorted needs to be provided \n
        :param A: the sequence to be sorted \n
        :param M: the range of values in A from 0...M inclusive
    """
    # first we initialize a list to store the number of times each integer occurs in order
    count = [0 for _ in range(M + 1)]
    for num in range(len(A)):
        count[A[num]] += 1
    # for instance, the number of times 0 occurs will given by count[0] and 5 will be given by count[5]
    for i in range(1, len(count)):
        count[i] += count[i-1]
    # cumulatively adding the frequency of each integer to later determine the index of their last occurence
    # shifting all elements one position to the right 
    # and setting the index of the first integer to 0 to get the index of the first occurence
    count.pop()
    count.insert(0, 0)
    sorted_array = [0 for _ in range(len(A))]
    for nm in A:
        sorted_array[count[nm]] = nm
        count[nm] += 1
    return sorted_array

# testing the algorithm
assert count_sort([], 0) == [], "fails on empty list"
assert count_sort([1, 0, 3, 2, 2, 5, 8, 7], 8) == [0, 1, 2, 2, 3, 5, 7, 8], "failed test 1"
assert count_sort([4, 2, 2, 8, 3, 3, 1], 8) == [1, 2, 2, 3, 3, 4, 8], "failed test 2"
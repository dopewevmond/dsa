import math
def bin_search(seq, low, high, key):
    """ Zero-index based binary search, eg. will return 5 for the 6th element"""
    if high < low:
        return low -1
    mid = math.floor(low + (high-low)/2)
    if key == seq[mid]:
        return mid
    elif key < seq[mid]:
        return bin_search(seq, low, mid - 1, key)
    else:
        return bin_search(seq, mid + 1, high, key)


a = [3, 5, 8, 10, 12, 15, 18, 20, 20, 50, 60]
print(bin_search(a, 0, 10, 50)) #should print 9 since the key 50, has an index of 9

b = [1, 2, 4, 5, 8, 15, 20]
print(bin_search(b, 0, 6, 9)) #should print 4 since 9 is greater than 8 (which has index of 4) but less than 15 (which has index of 5)
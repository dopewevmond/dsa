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
print(bin_search(a, 0, 10, 50))
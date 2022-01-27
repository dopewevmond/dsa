import math
def bin_search(seq, low, high, key):
    while high >= low:
        mid = math.floor(low + (high-low)/2)
        if key == seq[mid]:
            return mid
        elif key < seq[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low - 1


a = [3, 5, 8, 10, 12, 15, 18, 20, 20, 50, 60]
print(bin_search(a, 0, 10, 50)) #should print 9 since the key 50, has an index of 9

b = [1, 2, 4, 5, 8, 15, 20]
print(bin_search(b, 0, 6, 9)) #should print 4 since 9 is greater than 8 (which has index of 4) but less than 15 (which has index of 5)
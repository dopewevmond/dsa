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
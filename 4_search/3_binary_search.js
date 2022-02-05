const binary_search = (seq, low, high, key) => {
    if (high < low) return low - 1;
    mid = Math.floor(low + (high - low) / 2);
    if (seq[mid] == key) {
        return mid;
    }
    else if (seq[mid] > key) {
        return binary_search(seq, low, mid - 1, key);
    }
    else {
        return binary_search(seq, mid + 1, high, key);
    }
}

a = [3, 5, 8, 10, 12, 15, 18, 20, 20, 50, 60];
b = [1, 2, 4, 5, 8, 15, 20];

console.log(binary_search(a, 0, 10, 50)); //should print 9 since the key 50, has an index of 9
console.log(binary_search(b, 0, 6, 9)); //should print 4 since 9 is greater than 8 (which has index of 4) but less than 15 (which has index of 5)
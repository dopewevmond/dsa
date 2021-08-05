#define a function to compute fibonacci numbers

def fibonacci_naive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)

#the naive implementation is slow since it uses a recursive function each time that
#n is greater than 1
def fibonacci_efficient(n):
    if n <= 1:
        return n
    fib_list=[0,1]
    for _ in range(n-1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[-1]

print(fibonacci_efficient(10))
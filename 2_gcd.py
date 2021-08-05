#this program finds the greatest common divisor of two numbers

def find_gcd_naive(a, b):
    gcd = 0
    for i in range(1, a+b+1):
        if a%i==0 and b%i==0:
            gcd = i
    return gcd


def find_gcd_efficient(a, b):
    if b == 0:
        return a
    return find_gcd_efficient(b, a%b)
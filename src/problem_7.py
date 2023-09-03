from math import sqrt, floor
from sortedcollections import OrderedSet

primes = set()


def is_int(input_num):
    return input_num - floor(input_num) == 0


def is_prime(input_num):
    if input_num in primes:
        return True
    max = floor(sqrt(input_num))
    for num in range(2, max + 1):
        if is_int(input_num / num):
            return False
        num += 1
    primes.add(input_num)
    return True


def nth_prime(n):
    ord_primes = OrderedSet()
    num = 1
    while len(ord_primes) <= n:
        if is_prime(num):
            ord_primes.add(num)
        num += 1
    return ord_primes[n]


print(nth_prime(10001))

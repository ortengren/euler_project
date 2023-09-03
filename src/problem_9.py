from math import sqrt, floor, gcd

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


def are_coprimes(m, n):
    return gcd(m, n) == 1


def find_triple(sum):
    for a in range(1, floor(sum / 2)):
        for b in range(a, sum):
            if a + b + sqrt(a**2 + b**2) == sum:
                return a * b * sqrt(a**2 + b**2)


print(find_triple(1000))

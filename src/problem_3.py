from math import sqrt, floor

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

def find_largest_prime(input_num):
    if is_prime(input_num):
        return input_num
    num = 2
    while True:
        factor = input_num / num
        if is_int(factor):
            if is_prime(factor):
                return factor
            return find_largest_prime(factor)
        else:
            num += 1

print(find_largest_prime(600851475143))
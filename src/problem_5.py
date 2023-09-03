from math import sqrt, floor
from operator import countOf, mul
from functools import reduce

primes = set()


def is_int(input_num):
    return input_num - floor(input_num) == 0


def is_prime(input_num):
    if input_num in primes:
        return True
    elif input_num == 1 or input_num == 2:
        return True
    max = floor(sqrt(input_num))
    for num in range(2, max + 1):
        if is_int(input_num / num):
            return False
        num += 1
    primes.add(input_num)
    return True


def find_upper_bound(end):
    upper_bound = 1
    for i in range(1, end + 1):
        upper_bound *= i
    return upper_bound


def check_if_valid(end, num):
    for i in range(1, end + 1):
        if num % i != 0:
            return False
    return True


def get_prime_factors(num):
    factors = []
    if is_prime(num):
        factors.extend([1, int(num)])
        return factors
    for i in range(2, floor(num / 2) + 1):
        if not is_prime(i):
            continue
        if num % i == 0:
            factors.append(int(i))
            factors = factors + get_prime_factors(int(num / i))
            factors.sort()
            return factors


def get_primes_leq(input_num):
    leq_primes = set()
    for num in range(1, input_num + 1):
        if is_prime(num):
            leq_primes.add(num)
    return leq_primes


def get_smallest_multiple(input_num):
    prime_counter = {}
    factorization_list = []
    for num in range(1, input_num + 1):
        factorization_list.append(get_prime_factors(num))
    for factors in factorization_list:
        for factor in factors:
            factor_count = countOf(factors, factor)
            if not factor in prime_counter:
                prime_counter.update({factor: factor_count})
            elif countOf(factors, factor) > prime_counter.get(factor):
                prime_counter[factor] = factor_count
    values = []
    for key in prime_counter.keys():
        values.append(key ** prime_counter[key])
    smallest_multiple = reduce(mul, values)
    return smallest_multiple


print(get_smallest_multiple(20))

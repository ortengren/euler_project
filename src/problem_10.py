from eulerutils import PrimeMachine


def summation_of_primes(max_num):
    pm = PrimeMachine()
    n = 2
    curr_sum = 0
    while n < max_num:
        if pm.is_prime(n):
            curr_sum += n
        n += 1
    return curr_sum


print(summation_of_primes(2_000_000))

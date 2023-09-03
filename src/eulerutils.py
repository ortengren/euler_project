from math import sqrt, floor


class PrimeMachine:
    def __init__(self):
        self.primes = set()

    def is_int(input_num):
        return input_num - floor(input_num) == 0

    def is_prime(self, input_num):
        if input_num in self.primes:
            return True
        elif input_num == 2:
            return True
        elif input_num == 3:
            return True
        max = floor(sqrt(input_num))
        for num in range(2, max + 1):
            if self.is_int(input_num / num):
                return False
        self.primes.add(input_num)
        return True

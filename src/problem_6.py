def sum_of_squares(limit):
    return (2 * limit + 1) * (limit + 1) * limit / 6


def square_of_sums(limit):
    our_sum = limit * (limit + 1) / 2
    return our_sum**2


print(square_of_sums(100) - sum_of_squares(100))

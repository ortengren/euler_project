def sum_multiples(max):
    sum = 0
    for num in range(1, max):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum

print(sum_multiples(1000))


def even_fib_sum(max):
    fib_seq = {0:1, 1:2}
    index = 2
    sum = fib_seq.get(index - 1) + fib_seq.get(index - 2)
    even_sum = 2
    while sum <= max:
        fib_seq.update({index:sum})
        if sum % 2 == 0:
            even_sum += fib_seq.get(index)
        index += 1
        sum = fib_seq.get(index - 1) + fib_seq.get(index - 2)
    return even_sum

print(even_fib_sum(4000000))
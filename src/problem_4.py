def find_largest_palindrome(min, max):
    palindrome_max = 0;
    for i in range(min, max):
        for j in range(i, max):
            if str(i * j) [::-1] == str(i * j):
                if i * j > palindrome_max:
                    palindrome_max = i * j
    return palindrome_max

print(find_largest_palindrome(100, 1000))
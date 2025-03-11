def print_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                print('*', end=' ')
            else:
                print(j + 1 if j < i else j, end=' ')
        print()  # Move to the next line after each row


n = 4
print_pattern(n)
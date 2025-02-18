def all_numbers(n):
    for i in range(n, -1, -1):
        yield i
n = 5
for num in all_numbers(n):
    print(num)


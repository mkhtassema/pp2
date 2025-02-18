def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i
n = int(input("Enter a number: "))
even_numbers = ', '.join(map(str, even_generator(n)))
print(even_numbers)

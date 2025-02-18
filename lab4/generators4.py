def squares(a,b):
    for num in range(a,b+1):
        yield num ** 2
a,b = 1, 5
for square in squares(a, b):
    print(square)

def x(n):
    if n >= 0 and n <= 2:
        print('b')
        return n
    else:
        print('a')
        return x(n-1) + x(n-2) + x(n-3)

print(x(6))



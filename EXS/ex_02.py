def pierwsza(n):
    bool = True
    if n < 1: bool = False
    for i in range(n-1, 2, -1):
        if n % i == 0:
            bool = False
            break
    return bool

print(pierwsza(1))

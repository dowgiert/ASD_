from z_1 import silnia


def NEWTON2(n, m):
    x = 1
    y = 0
    for i in range(n-m + 1, n+1):
        x *= i
        y += 1
    print(y)
    x = x/silnia(m)
    y = y + m
    return x, y


x, y = NEWTON2(25, 12)
print(f"Wynik to:{x}, liczba wykonanych mnożeń {y}")

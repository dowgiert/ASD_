def silnia(n):
    x = 1
    if n == 0 or n == 1:
        return 1
    else:
        x = n * silnia(n-1)
    return x


def iteracyjnie(n):
    x = 1
    for i in range(1, n+1):
        x = x * i

    return x


if __name__ == "__main__":
    print(f"iteracyjnie {iteracyjnie(5)}")
    print(f"rekurencyjnie {silnia(5)}")

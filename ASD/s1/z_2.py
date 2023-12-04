from z_1 import silnia


def newton1(n, m):
    x = silnia(n)/(silnia(m)*(silnia(n-m)))
    l = (n) + (m) + (n-m) + 2
    return [x, l]


if __name__ == "__main__":
    x, l = newton1(25, 12)
    print(f"Wynik {x} liczba mnożeń {l}")

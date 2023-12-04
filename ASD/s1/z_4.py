k = 0#O(2^n)
def NEWTON3(n, m):
    global k
    if n < m:
        return "zle wartosci"
    elif n == m or m == 0:
        k += 1
        return 1
    elif n-1 == m or m == 1:
        k += 1
        return n
    else:
        return NEWTON3(n-1, m-1) + NEWTON3(n-1, m)


print(NEWTON3(25, 12))
print(f"K wynosi {k-1}.")
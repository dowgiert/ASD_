def NEWTON5(n, m):
    SN = [[0] * (n + 1) for _ in range(n + 1)]
    SN[0][0] = 1
    additions = 0
    for i in range(1, n + 1):
        for j in range(i + 1):
            if j == 0:
                SN[i][j] = 1
            else:
                SN[i][j] = SN[i - 1][j] + SN[i - 1][j - 1]
                additions += 1
    print(SN)
    return SN[n][m], additions
n = 25  
m = 12
wynik, suma = NEWTON5(n, m)
print(wynik)
print(suma)
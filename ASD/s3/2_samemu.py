def szyfr(slowo1, slowo2):
    slowo1 = slowo1.lower()
    slowo2 = slowo2.lower()
    lista = {}
    for litera in slowo1:
        if litera not in lista:
            lista[litera] = 1
        else:
            lista[litera] += 1
    lista2 = {}
    for litera in slowo2:
        if litera not in lista2:
            lista2[litera] = 1
        else:
            lista2[litera] += 1

    suma = {}
    for i in lista:
        for k in lista2:
            if i == k:
                if i not in suma:
                    if lista[i] >= lista2[k]:
                        suma[i] = lista2[k]
                    else:
                        suma[i] = lista[i]
    napis = ''.join([i * suma[i] for i in suma])
    lista3 = lista2

    klucze_do_usuniecia = [key for key in lista2 if key not in suma]
    for key in klucze_do_usuniecia:
        del lista3[key]
    napis2 = ''.join([i * lista3[i] for i in lista3])

    return napis, napis2

def lcs(a, b):
    # Tworzenie tablicy do przechowywania długości największych wspólnych podciągów
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    # Wypełnienie tablicy
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_string = ""
    i, j = len(a), len(b)
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs_string = a[i - 1] + lcs_string
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_string, len(lcs_string)

print(szyfr('kkaroll', "roakkp"))
napis, napis2 = szyfr('kkaroll', "roakkp")
print(lcs(napis, napis2))
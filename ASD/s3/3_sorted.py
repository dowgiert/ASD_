def kinoman(lista):
    if len(lista)>=1:
        k = 1
        ktore = [lista[0]]
        seans = lista[0]
        lista = sorted(lista, key=lambda x: x[1])
        for numer in range(0, len(lista)):
            if seans[1] <= lista[numer][0]:
                k+=1
                seans = lista[numer]
                ktore.append(seans)
    else:
        if len(lista) == 0:
            print("Nie ma filmow")
            exit()
    return k, ktore

r =  [[9,11],[8,12],[11,13],[10,12],[11,15],[12,16],[14,17],
[16,18],[15,19],[18,21],[19,21]]
print(f"Posortowana funkcja kinomanem {kinoman(r)}")
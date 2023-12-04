def quick_sort_r(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_r(arr, low, pi)
        quick_sort_r(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[low][1]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i][1] < pivot:
            i += 1
        j -= 1
        while arr[j][1] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

r = [[9, 11], [8, 12], [11, 13], [10, 12], [11, 15], [12, 16], [14, 17], 
     [16, 18], [15, 19], [18, 21], [19, 21]]

quick_sort_r(r, 0, len(r) - 1)
print("Posortowana tablica:", r)

#-----------------------------------------------------------------------
def kinoman(lista):
    if len(lista)>=1:
        k = 1
        ktore = [lista[0]]
        seans = lista[0]
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

print(f"funkcja kunoman {kinoman(r)}")
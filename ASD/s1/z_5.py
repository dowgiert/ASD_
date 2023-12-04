def NEWTON4(n):
    k = 0
    res = [[1]]
    for i in range(n-1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1])+1):
            row.append(temp[j] + temp[j+1])
            k += 1
        res.append(row)
    return res, k


res, k = NEWTON4(5)
print(res, k)

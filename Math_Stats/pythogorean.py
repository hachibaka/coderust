def triplets_3sum(arr):
    n = len(arr)

    output = []
    for i in range(n):
        for j in range(i+1,n):
            a = arr[i]**2
            b = arr[j]**2
            c = (a + b)**0.5
            if c.is_integer() and int(c) in arr:
                output.append(sorted([arr[i],arr[j],int(c)]))

    return output

def triplets_3sum_sort(arr):
    arr.sort()
    n = len(arr)
    output = []
    for i in range(n):
        if arr[i] == 0:
            continue
        c2 = arr[i]**2
        j = 0
        k = n-1
        while j < k:
            if j == i or arr[j] ==0:
                j += 1
                continue
            if k == i or arr[k] ==0:
                k -= 1
                continue
            a2 = arr[j]**2
            b2 = arr[k]**2
            if a2 + b2 == c2:
                output.append([arr[i],arr[j],arr[k]])
                break
            elif a2 + b2 - c2 > 0:
                k -= 1
            else:
                j += 1
    return output


a = [4, 16, 1, 2, 3, 5, 6, 8, 25,10]*100
print(triplets_3sum(a))
print(triplets_3sum_sort(a))

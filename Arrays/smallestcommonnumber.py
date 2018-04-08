def smallest_common_number(a, b, c):
    i = j = k = 0
    while i < len(a) and j < len(b) and k < len(c):
        
        if a[i] == b[j] and b[j] == c[k]:
            return a[i]

        if a[i] <= b[j] and a[i] <= c[k]:
            i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j += 1
        elif c[k] <= b[j] and c[k] <= a[i]:
            k += 1
    return -1

a = [6,7,10,25,30,63,64]
b = [-1,4,5,6,7,8,50]
c = [  1,6,10,14]
print(smallest_common_number(a,b,c))

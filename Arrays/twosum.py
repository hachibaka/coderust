a = [5,7,1,2,8,4,3]
def twosum(a,n):
    d = {}
    indices = []
    for i,val in enumerate(a):
        if n-val in d:
            indices.append((d[n-val],i))
        else:
            d[val] = i
    return indices

print(twosum(a,10))

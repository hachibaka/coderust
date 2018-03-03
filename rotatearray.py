a = [-6,-5,-3,-1,4,8,9,10,11]


def rotate(a,n):
    length = len(a)
    rarray = [None]*length
    for i,val in enumerate(a):
        if n < 0:
            rarray[(i+n+length)%length] = a[i]
        else:
            rarray[(i+n)%length] = a[i]
    return rarray

def rotate_slice(a,n):
    if n < 0:
        n = abs(n)
        return a[n:]+a[:n]
    else:
        n = n%length
        return a[-n:]+a[:len(a)-n]


print(a)
print("array rotate:",rotate(a,3))
print("Slice rotate:",rotate_slice(a,3))
print("array rotate:",rotate(a,-1))
print("Slice rotate:",rotate_slice(a,-1))
print("array rotate:",rotate(a,-3))
print("Slice rotate:",rotate_slice(a,-3))
print("array rotate:",rotate(a,1))
print("Slice rotate:",rotate_slice(a,1))

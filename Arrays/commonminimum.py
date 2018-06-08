import random

def generate_array(minval,maxval,numofelements):
    return [random.randint(minval,maxval) for _ in range(numofelements)]

def common_minimum(a,b,c):
    i = j =k = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] and b[j] == c[k]:
            return a[i]
        maxval = max(a[i],b[j],c[k])
        print(maxval)

        if maxval == a[i]:
            if a[i] != b[j]:
                j +=1
            elif a[i] != c[k]:
                k += 1
        elif maxval == b[j]:
            if a[i] != b[j]:
                i +=1
            elif b[i] != c[k]:
                k += 1
        else:
            if a[i] != c[k]:
                i +=1
            elif b[j] != c[k]:
                j += 1

    return None

a = [-4,-2,-1,0,2,6,11,11]
b = [-6,-5,-3,-1,4,8,9,10,11]
c = [-8,-3,2,3,4,8,9,10,11]

answer = common_minimum(a,b,c)
if not answer:
    print("No Common Element")
else:
    print("Common element between three array is ",answer)

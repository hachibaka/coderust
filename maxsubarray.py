def kadane(a):
    maxsum = submax = a[0]
    for x in a[1:]:
        print(submax,x,submax+x)
        submax = max(x,submax+x)
        maxsum = max(maxsum,submax)
    return maxsum

a = [-2,-3,4,-1,-2,1,5,-3]
print(kadane(a))

import random, math

def generate_array(n):
    return [random.randint(1,100) for _ in range(n)]

a = generate_array(40)

def kthpermutation(arr,k):
    output = []
    while arr:
        n = len(arr)
        blocksize = math.factorial(n-1)
        print(blocksize,k)
        blockpos = (k-1)// blocksize
        output.append(arr[blockpos])
        del arr[blockpos]
        k = k - blockpos*blocksize
    return output

print(a)
#print(kthpermutation(a,4))
print(kthpermutation(a,400))

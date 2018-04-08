import random, time
def binarysearchrec(a,key,low,high):
    if low > high:
        return -1
    mid = low + ((high - low) //2)
    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return binarysearchrec(a,key,low,mid-1)
    else:
        return binarysearchrec(a,key,mid+1,high)


def binary_search_rec(a,key):
    return binarysearchrec(a,key,0,len(a)-1)

def binary_search_iter(a,key):
    low = 0
    high = len(a) - 1
    numiter = 0
    while low <= high:
        numiter += 1

        mid = low + ((high - low) //2)
        if a[mid] == key:
            print("number of iterations ",numiter)
            return mid
        if a[mid] < key:
            low = mid + 1
        else:

            high = mid -1
    print("number of iterations ",numiter)
    return -1



def generate_array(numofelements):
    return [random.randint(-1000,1000) for _ in range(numofelements)]


start_time  = time.time()
print("Starting recursive function calling 10 times")
for _ in range(10):
    a = generate_array(100000)
    a.sort()
    key = random.randint(-1000,1000)
    print(key,binary_search_rec(a,key),a.index(key))
end_time = time.time()
print("Ended  recursive function calling 10 times and time taken is ", end_time - start_time)


random.seed(0)
start_time  = time.time()
print("Starting Iterative function calling 10 times")
for _ in range(10):
    a = generate_array(100000)
    a.sort()
    key = random.randint(-1000,1000)
    print(key,binary_search_iter(a,key),a.index(key))
end_time = time.time()
print("Ended  Iterative function calling 10 times and time taken is ", end_time - start_time)

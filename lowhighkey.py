def binary_search_modified(a,key):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + (high - low)//2
        if a[mid] > key:
            high = mid -1
        elif a[mid] < key:
            low = mid + 1
        else:
            low = high = mid
            while low -1 >=0 and a[low-1] == key:
                low -=1
            while high +1 <len(a) and a[high+1] == key:
                high +=1
            return low, high

    return -1,-1

a = [1,2,5,5,5,5,5,5,5,5,20]
print(binary_search_modified(a,5))
print(binary_search_modified(a,20))

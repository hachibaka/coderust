def quicksort(a,low=0,high=None):
    if not high:
        high = len(a) - 1
    if low < high:
        pivot_index = partition(a,low,high)
        quicksort(a,low,pivot_index-1)
        quicksort(a,pivot_index+1,high)


def partition(a,low,high):
    i = low + 1
    j = high
    pivot = a[low]
    print(a)
    while i < j:
        while i <= j and a[i] < pivot:
            i += 1

        while a[j] > pivot:
            j -= 1

        if i < j:
            a[i], a[j] = a[j] , a[i]
        else:
            break
    a[low],a[j] = a[j], a[low]
    print(a)
    return j

a = [54,26,93,17,77,31,44,55,20]
quicksort(a)

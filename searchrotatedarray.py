import random, time
def binary_search(arr, st, end, key):

  # assuming all the keys are unique.

  if st > end:
    return -1

  mid = st + (end-st)//2

  if arr[mid] == key:
    return mid

  if (arr[st] < arr[mid] and
        key < arr[mid] and
        key >= arr[st]):
    return binary_search(arr, st, mid-1, key)
  elif (arr[mid] < arr[end] and
           key > arr[mid] and
           key <= arr[end]):
    return binary_search(arr, mid+1, end, key)
  elif arr[st] > arr[mid]:
    return binary_search(arr, st, mid-1, key)
  elif arr[end] < arr[mid]:
    return binary_search(arr, mid+1, end, key)

  return -1

def binary_search_rotated(arr, key):
  return binary_search(arr, 0, len(arr)-1, key)

def linear_search(arr,key):
    try:
        return arr.index(key)
    except ValueError:
        return -1

def generate_array(n):
    return sorted([random.randint(-1000,1000) for _ in range(n)])

def rotate_array(arr):
    k = random.randint(1,len(arr)-1)
    n = len(arr)
    return arr[n-k:] + arr[:n-k]

a = generate_array(2000000)
a = rotate_array(a)
start_time = time.time()
print(binary_search_rotated(a,100))
print("Time taken for binary search is ",time.time() - start_time)
start_time = time.time()
print(linear_search(a,100))
print("Time taken for Linear search is ",time.time() - start_time)

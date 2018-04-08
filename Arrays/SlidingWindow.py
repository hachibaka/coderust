import random
from collections import deque


def generate_array(minval,maxval,numofelements):
    return [random.randint(minval,maxval) for _ in range(numofelements)]



def sliding_max_naive(a,k):
    if len(a) < k:
        print("Nomax")
        return
    for i in range(len(a)-k+1):
        print(max(a[i:i+k]),end=" ")
    print()

def sliding_max_linkedlist(a,k):
    window = deque()
    j = 0
    for i in range(k):
        while window and a[i] >= a[window[-1]]:
            window.pop()
        window.append(i)
    print(a[window[0]], end = ' ')

    for i in range(k,len(a)):
        while window and a[i] >= a[window[-1]]:
            window.pop()

        if window and window[0] <= i -k:
            window.popleft()

        window.append(i)

        print(a[window[0]],end= ' ')
    print()




a = generate_array(-1000,1000,10)
print(a)
sliding_max_naive(a,3)
sliding_max_linkedlist(a,3)

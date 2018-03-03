import time
a = [1,10,20,0,59,63,0,88,0] * 900000


def readers_writers(b):
    #b = a[:]
    reader = len(b) -1
    writer = len(b) -1
    while writer >=0:
        if reader >= 0 and b[reader] != 0:
            b[writer] = b[reader]
            writer -= 1
            reader -= 1
        elif reader >= 0 and b[reader] ==0:
            reader -=1
        elif reader <0:
            b[writer] = 0
            writer -= 1
    return b


def slice_sol(a):
    return [x for x in a if x ==0] + [x for x in a if x !=0]

start_time = time.time()
readers_writers(a)
print("Total time taken for readers writers solution",time.time()-start_time)
start_time = time.time()
slice_sol(a)
print("Total time taken for slice solution",time.time()-start_time)

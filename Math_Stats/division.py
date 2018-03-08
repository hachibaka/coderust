import time

def int_div(divident, divisor):
    i = 0
    while divident > 1:
        divident = divident - divisor
        i += 1
    return i

def int_div_bit(x, y):

    if y == 0:
        return -1
    if y == 1:
        return x
    if y > x:
        return 0
    if y == x:
        return 1

    q = 1
    val = y

    while  val < x:
        q = q << 1
        val <<= 1

    if  val > x:
        val >>= 1
        q >>=1
        return q + int_div_bit(x-val,y)
    return q

start_time = time.time()
print(int_div(1,2))
print(int_div(2,2))
print(int_div(20,2))
print(int_div(20,5))
print(int_div(100,5))
print(int_div(1,5))
print(int_div(40000000,3))

print("Ended naive method in ", time.time() - start_time)
start_time = time.time()
print(int_div_bit(1,2))
print(int_div_bit(2,2))
print(int_div_bit(20,2))
print(int_div_bit(20,5))
print(int_div_bit(100,5))
print(int_div_bit(1,5))
print(int_div_bit(40000000,3))
print("Ended bit method in ", time.time() - start_time)

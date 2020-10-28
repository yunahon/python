def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def fib2(n):
    m = {0:0,1:1}
    if n not in m:
        m[n] = fib2(n-1) + fib2(n-2)
    return m[n]

def fib3(n):
    if n == 0:
        return n
    else:
        previous = 0
        current = 1
        for i in range(n-1):
            new = previous + current
            previous = current
            current = new
    return current


n = 33
print(fib(n))
print(fib2(n))
print(fib3(n))
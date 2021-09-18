#Python Program for n-th Fibonacci number

def fibonacci(n):
    a,b = 0,1
    if n == 0:
        return a
    if n == 1:
        return b;
    else:
        for i in range(2,n+1):
            fibo = a+b
            a = b
            b = fibo
    return b

val = fibonacci(6)
print (val)

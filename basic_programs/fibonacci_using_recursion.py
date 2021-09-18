#Python Program for n-th Fibonacci number

def fibonacci(n):
    if n ==0:
        return 0
    if n ==1:
        return 1;
    else:
        return fibonacci(n-1) + fibonacci(n-2)

val = fibonacci(6)
print (val)

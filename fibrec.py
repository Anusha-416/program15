n=8
def fib(n):
    if n==0:
        return n
    elif n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
for i in range(n):
    print(fib(i))

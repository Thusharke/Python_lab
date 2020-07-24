

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1)+fib(n-2)


length = int(input("enter the length of the series : "))
for i in range(length+1):
    print(fib(i), end=" ")






# recursive and iterative fibonacci

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-2)+fib(n-1)


def ifib(n):
    '''iterative fibonacci'''
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n+1):
        f = a+b
        print(i,f)
        a,b = b,f

print('iterative - - - - - - ')
ifib(20)

print('and now recursive - - - - - - ')
print(7,fib(7))
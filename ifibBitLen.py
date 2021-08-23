def ifib(n):
    '''iterative fibonacci'''
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n+1):
        f = a+b
        print(i,f, f.bit_length())
        a,b = b,f

ifib(60)
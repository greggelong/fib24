def ifib(n):
    '''iterative fibonacci'''
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n+1):
        f = a+b
        fr = reduce(f)
        print(i,f, fr)
        a,b = b,f


def reduce(n):
    '''use list comprehension '''
    nlist = [int(x) for x in str(n)]
    #print(nlist, len(nlist))
    count =0
    rlist = []
    while len(nlist) > 1:
        count +=1
        sumit = sum(nlist)
        rlist.append(sumit)
        #print(sumit)
        nlist = [int(x) for x in str(sumit)]
        #print(nlist, len(nlist))
    return sum(nlist), count, rlist # returns the sum of a single list item converting it to int



## prints number, fibonacci and (fibonacci reduction and number of times reduced, and [list of reductions])
ifib(500)   


 
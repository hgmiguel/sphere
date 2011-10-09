#!/usr/bin/python
#import math,sys

'''
raw times: 1.35 1.35 1.35
100 loops, best of 3: 13.5 msec per loop
'''
def optimizacion_1():
    n=int(raw_input())

    numbers=[]
    results={1:1,2:2,3:6,4:24,5:120,6:720,7:5040}
    while n>0:
       num=int(raw_input())
       numbers.append(num)
       n-=1

    result=5040
    for x in range(8,max(numbers)+1):
        result*=x
        results[x]=result


    for x in numbers:
        print results[x]


    #sys.stdin.seek(0)

def fact1(n):  return reduce(lambda x,y: x*y,  xrange(1,n+1),1)
'''
raw times: 1.41 1.42 1.42
100 loops, best of 3: 14.1 msec per loop
'''
def sin_optimizar():
    n=int(raw_input())

    print n
    while n>0:
        num=int(raw_input())
        print math.factorial(num)
        n-=1

    sys.stdin.seek(0)


def optimizacion_2():
    n=int(raw_input())
    cache={1:1,2:2,3:6,4:24,5:120,6:720}

    print n
    while n>0:
        num=int(raw_input())
        print mfactorial(num,cache)
        n-=1

    sys.stdin.seek(0)

def mfactorial(n, _factcache={}):
    if n-1 not in _factcache:
        _factcache[n]=math.factorial(n)
        _factcache[n+1]=(n+1)*math.factorial(n)
    elif n not in _factcache:
        #print "entre"
        _factcache[n]=n*_factcache[n-1]
    return _factcache[n]

if __name__ == "__main__":
    optimizacion_1()

#!/usr/bin/python
import sys
#import random

'''
python -m timeit 'import palin' 'palin.primera_aprox()' < palin.in ; ./palin.py < palin.in > palin.out.cmp; diff palin.out palin.out.cmp
10 loops, best of 3: 55.7 msec per loop bad
10 loops, best of 3: 97.3 msec per loop ok
100 loops, best of 3: 3.44 msec per loop sin los print
100 loops, best of 3: 3.42 msec per loop rehaciendo el has_cuentas
100 loops, best of 3: 4.5 msec per loop
100 loops, best of 3: 3.41 msec per loop

con un buen de numeros...
10 loops, best of 3: 2.49 sec per loop

10 loops, best of 3: 2.21 sec per loop #con abs
10 loops, best of 3: 2.64 sec per loop

'''

def has_cuentas(numero,length=1):
    #numero=list(numero)
    #print "numero %s, l%s y r%s" %(numero, l, r)
    #length=len(numero)
    while True:
        l=int(numero[0])
        r=int(numero[-1])
        if l == r:
            break
        elif r > l:
            l+=10
        
        numero=int("".join(numero)) + (l - r)
        numero=list(str(numero))
        #if length > len(numero):
        if length > len(numero):
            numero.insert(0,'0')

    return numero


def primera_aprox():
    n = int(raw_input())
    #n = 1
    while n != 0:
        numero=list(str(int(raw_input()) +1))

        numero=has_cuentas(numero)
        length=len(numero)
        mitad=length/2
        pasada=1
        lados=[]
        while pasada < mitad:
            lados+=numero[0:1]
            numero=numero[1:-1]
            length-=2
            numero=has_cuentas(numero,length)
            pasada+=1
        
        print "".join(lados + numero + lados[::-1])

        n-=1

    sys.stdin.seek(0)

def genera_numeros(numeros={}):
    t=int(random.random() * 1000000)
    tc=t
    while True:
        tc+=1
        if str(tc) == str(tc)[::-1]:
            numeros[t]=tc
            break




if __name__ == '__main__':
    primera_aprox()

#!/usr/bin/python
import sys,random

'''
10 loops, best of 3: 55.7 msec per loop
'''
def has_cuentas(numero):
    numero=list(numero)
    l=numero[0]
    r=numero[-1]
    f=False

    print "numero %s, l%s y r%s" %(numero, l, r)
    length=len(numero)
    while l != r:
        if int(l) == 0:
            #f=True
            l=10
        if int(r) > int(l):
            numero=int("".join(numero)) + (int(l)+10 - int(r))
        else:
            numero=int("".join(numero)) + (int(l) - int(r))
        print "numoero sin el strint",numero
        numero=list(str(numero))
        print "length:%s len:%s" %(length,len(numero))
        if length > len(numero):
            numero.insert(0,'0')
        #else:
        l=numero[0]
        r=numero[-1]
        print "numero %s, l%s y r%s" %(numero, l, r)
           

    return "".join(numero)


def primera_aprox():
    n = int(raw_input())
    #n = 1
    while n != 0:
        numero=int(raw_input()) +1
        print "numero inicial %s" %(numero)

        numero=has_cuentas(str(numero))
        pasada=1
        while numero != "".join(list(numero)[::-1]):
            print "pasada %s, numero:%s" %(pasada, numero)
            numero=list(numero)
            lados=numero[0:pasada]
            numero=numero[pasada:-(pasada)]
            print "despues de recortarlo %s" %("".join(numero))
            numero=has_cuentas("".join(numero))
            numero="".join(lados) + str(numero) + "".join(lados[::-1])
            pasada+=1
        
        print "el buenas",numero

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
    #numeros={}
    #for x in xrange(1,100):
    #    genera_numeros(numeros)
    
    #for x in numeros:
    #    print "in:%s,out:%s" % (x,numeros[x])
    primera_aprox()

#!/usr/bin/python

def has_cuentas(numero,numeros,length=1):
    numero_s="".join(numero)
    if numero_s in numeros:
        return numeros[numero_s]

    while True:
        l=int(numero[0])
        r=int(numero[-1])
        if l == r:
            break
        elif r > l:
            l+=10
        
        numero=int("".join(numero)) + (l - r)
        numero=list(str(numero))
       
        if length > len(numero):
            numero.insert(0,'0')

    numeros[numero_s]=numero
    return numero


def primera_aprox():
    import sys
    data = sys.stdin.readlines()
    numeros={}
    for i in xrange(1, len(data)):
        numero=list(str(int(data[i]) +1))

        numero=has_cuentas(numero, numeros)
        length=len(numero)
        mitad=length/2
        pasada=1
        lados=[]
        while pasada < mitad:
            lados+=numero[0:1]
            numero=numero[1:-1]
            length-=2
            numero=has_cuentas(numero, numeros, length)
            pasada+=1
        
        print "".join(lados + numero + lados[::-1])


    sys.stdin.seek(0)
        

if __name__ == '__main__':
    primera_aprox()

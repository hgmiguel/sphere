#!/usr/bin/python
'''
Input:
    2
    808
    2133
    3 
    9 
    53936 
    53236 
    67775 
    99 
    999 
    6339 
    875111 
    6997 
Output:
    818
    2222
    4 
    11 
    54045 
    53335 
    67776 
    101 
    1001 
    6446 
    875578 
    7007 
'''

'''
Mas malo que nada
print n
while n != 0:
    numero=raw_input()
    numero=list(numero)
    l=numero[0]
    r=numero[-1]

    if int(r)+1 > int(l):
        numero[0]=str(int(l)+1)
    else:
        numero[-1]=str(int(r)+1)

    print numero
    n-=1

'''
def has_cuentas(numero):
    numero=list(str(numero))
    l=numero[0]
    r=numero[-1]

    while l != r:
        if int(r) > int(l):
            numero=int("".join(numero)) + (int(l)+10 - int(r))
        else:
            numero=int("".join(numero)) + (int(l) - int(r))
        print "numero sin el strint",numero
        numero=list(str(numero))
        l=numero[0]
        r=numero[-1]
        print "numero %s, l%s y r%s" %(numero, l, r)
           

    return int("".join(numero))


def primera_aprox():
    n = int(raw_input())
    #n = 5
    while n != 0:
        numero=int(raw_input()) +1
        print "numero inicial %s" %(numero)

        numero=has_cuentas(numero)
        pasada=1
        while str(numero) != "".join(list(str(numero))[::-1]):
            print "pasada %s, numero:%s" %(pasada, numero)
            numero=list(str(numero))
            lados=numero[0:pasada]
            numero=numero[pasada:-(pasada)]
            print "despues de recortarlo %s" %("".join(numero))
            numero=has_cuentas(int("".join(numero)))
            numero=int("".join(lados) + str(numero) + "".join(lados[::-1]))
            pasada+=1
        
        print "el buenas",numero

        n-=1
'''
        print "despues del primero %s" %(numero)
        if str(numero) == "".join(list(str(numero))[::-1]):
            print "jjjjjj",numero
        else:
            numero=list(str(numero))
            lados=numero[0],numero[-1]
            numero=numero[1:-1]
            print "despues de recortarlo %s" %("".join(numero))
            numero=has_cuentas(int("".join(numero)))
            print "segunda",lados[0] + str(numero) + lados[1]
  '''          



if __name__ == '__main__':
    primera_aprox()

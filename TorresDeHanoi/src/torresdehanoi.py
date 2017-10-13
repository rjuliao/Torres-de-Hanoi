# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from time import time

def hanoiR(n, a, b, c):
    if n == 1:
        print("Movemos un disco de : "+ a +" a "+ b)
    else:
        hanoiR(n-1, a, c, b)
        print("Movemos un disco de : "+ a +" a "+ b)
        hanoiR(n-1, c, b, a)
        
def hanoiI(n, a, b, c):
    pa = [0 for x in range(n)]
    pb = [0 for x in range(n)]
    pc = [0 for x in range(n)]
    pn = [0 for x in range(n)]
    top = 0;
    sw = False
    aux = ""
    
    while(n >0 and sw == False):
        while(n > 1):
            top += 1
            pn[top] = n
            pa[top] = a
            pb[top] = b
            pc[top] = c
            n -= 1
            aux = b
            b = c
            c = aux
        print("Mover disco de: " + a +" --> "+ b)
        sw = True
        if(top > 0):
            n = pn[top]
            a = pa[top]
            b = pb[top]
            c = pc[top]
            top -= 1
            print("Mover disco de: "+ a +" --> "+b)
            n -= 1
            aux = a
            a = c
            c = aux
            sw = False;
    
if __name__ == "__main__":
    print( "Ingrese el numero de discos: ")
    n = int(input())
    print "Recursivo"
    tir = time()
    hanoiR(n, "A", "B", "C")
    tfr = time()
    ttr = tfr - tir
   
    print "Iterativo"
    tii = time()
    hanoiI(n, "A", "B", "C")
    tfi = time()
    tti = tfi - tii
    
    
    print "La diferencia de tiempos es: "
    print "Iterativo: "+ str(ttr) +" seg"
    print "Recursivo: "+ str(tti) +" seg"

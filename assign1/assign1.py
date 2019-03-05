import time
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibItHelper(n,a,b):
    if n==0:
        return a
    elif n==1:
        return b
    else:
        return fibItHelper(n-1,b,a+b)

def fibIt(n):
    return fibItHelper(n,0,1)

def main():
    for i in range(0,1000):
        start = time.time()
        #f=fib(i)
        end = time.time()
        start2 = time.time()
        f2 = fibIt(i)
        end2 = time.time()
        #print("Calculated fib(",i,") =",f," in ",end-start," seconds, and fibIt(",i,") =",f2," in ",end2-start2, " seconds")
        print(end2-start2)

main()
"""
@Author : Jacob Verdesi   jxv3386@rit.edu
Algo Homework Assign0

"""
def r(xs):
    if not xs:
        return
    else:
        return xs[0]+r(xs[1:])

def prod(m,n):
    if m==0:
        return 0
    else:
        return prod((m-1),n)+n

def fastPow(b,k):
    if k==0:
        return 1
    elif k%2==0:
        return fastPow(b^2,k-1)
    else:
        return fastPow(b^2,k-1)*b

def prodAccum(m,n,a):
    if m==0:
        return a
    else:
        return prodAccum(m-1,n,n+a)

def min(x, y):
    if not x and not y:
        return None
    elif not x:
        return y
    elif not y:
        return x
    elif x>y :
        return y
    else:
        return x

def circlePlus(x,y):
    if x is None or y is None:
        return None
    else:
       return x+y

def minChange(a,ds):
    if a==0:
        return 0
    elif not ds:
        return None
    else:
        d = ds[0]
        if(d > a):
           return minChange(a,ds[1:])
        else:
           return min(circlePlus(1,minChange(a-d,ds)),minChange(a,ds[1:]))

def greedyMinChange(a,ds):
    if a==0:
        return 0
    elif not ds:
        return None
    else:
        d = ds[0]
        if (d > a):
            return greedyMinChange(a, ds[1:])
        else:
            q=int(a/d)
            r=a-(q*d)
            return circlePlus(q,greedyMinChange(r,ds[1:]))



def powIt(b,n):
    total=1
    for i in range(n):
        total=total*b
        n-=1

    return total


def main():
    list=[25,10,5,1]
    print(minChange(74,list))
    #print(greedyMinChange(74, list))
    #print(powIt(3,0))
if __name__ == '__main__':
    main()

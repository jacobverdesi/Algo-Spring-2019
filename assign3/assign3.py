import math
import random
#github test

def searchHelp(a,v,l,h):
    m=math.floor(((h-l)/2))
    mPrime=m+l
    printSearch(a,v,l,h,m,mPrime)
    if l>h:
        return False
    elif v==a[mPrime]:
        return True
    elif v<a[mPrime]:
        return searchHelp(a,v,l,mPrime-1)
    else:
        return searchHelp(a,v,mPrime+1,h)
def printSearch(a,v,l,h,m,mPrime):

    i=0
    for num in a:
        if num == v:
            print(" "+'\033[41m'+str(v)+'\033[0m',end="")
        elif l==i:
            print(" "+'\033[42m'+str(l)+'\033[0m',end="")
        elif m==num:
            print(" "+'\033[43m'+str(m)+'\033[0m',end="")
        elif mPrime==num:
            print(" "+'\033[45m'+str(mPrime)+'\033[0m',end="")
        elif h == i:
            print(" "+'\33[104m'+str(h)+'\033[0m',end="")
        else:
            print(' '+str(num),end="")
        i+=1
    print("")

def search(a,v):
    return searchHelp(a,v,0,len(a)-1)

def searchWhile(a,v):
    l=0
    h=len(a)-1
    while l<=h:
        m = math.floor(((h - l) / 2))
        mPrime = m + l

        printSearch(a, v, l, h, m, mPrime)
        if v == a[mPrime]:
            return True
        elif v < a[mPrime]:
            h= mPrime - 1

        else:
            l= mPrime + 1
    return False

def sumComp(n1,n2,x):
    return (n1+n2)==x

def printSearchSum(a,v,l,h,sumC):
    i=0
    for num in a:

        if l==i:
            print(" "+'\033[45m'+str(num)+'\033[0m',end="")
        elif h == i:
            print(" "+'\33[46m'+str(num)+'\033[0m',end="")
        else:
            print(' '+str(num),end="")
        i+=1
    if sumC== v:
        print(" = " + '\033[41m' + str(sumC) + '\033[0m')
    else:
        print(" = "+'\033[43m'+str(sumC)+'\033[0m')

def sortedHasSumHelp(a,v,l,h,acc):
    sumC=a[l]+a[h]
    printSearchSum(a,v,l,h,sumC)

    if l > h:
        return False , acc
    elif v == sumC:
        return True,l,h,acc
    elif v < sumC:
        return sortedHasSumHelp(a, v, l, h - 1,acc+1)
    else:
        return sortedHasSumHelp(a, v, l + 1, h,acc+1)

def sortedHasSum(s,x):
    return sortedHasSumHelp(s,x,0,len(s)-1,0)
     # found=False
     # for num in s:
     #     for num2 in s[s.index(num)+1:]:
     #         print(num,num2)
     #         if num is not num2 and sumComp(num,num2,x):
     #             found=True
     #             #print(num,num2)
     # return found


def hasSum(s,x):
    return sortedHasSum(sorted(s),x)

def partition(a,l,h):
    x=a[h]
    i=l-1
    j=l
    while j<h:
        if a[j]<=x:
            i+=1
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j+=1
    temp = a[i+1]
    a[i+1] = a[h]
    a[h] = temp
    return i+1

def quicksortHelper(a,l,h):
    if l<h:
        m=partition(a,l,h)
        quicksortHelper(a,l,m-1)
        quicksortHelper(a,m+1,h)

    return a
def quicksort(a):
    return quicksortHelper(a,0,len(a)-1)

def main():
    a=[7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    #print(sortedHasSum(a, 25))
    a=sorted(a, key = lambda x: random.random() )
    print(a)
    # for i in range(-10,10):
    #     a.append(i)
    #print(search(a,97))
    #printColors()
    #print(hasSum(a,25))
    #print(searchWhile(a,5))
    print(quicksort(a))
main()
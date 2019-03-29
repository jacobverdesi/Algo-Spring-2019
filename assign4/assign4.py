def max2(num1,num2):
    return (num1+num2+(abs(num1-num2)))/2


def swap(lst,i,j):
    lst2=lst
    temp = lst2[i]
    lst2[i] = lst[j]
    lst2[j] = temp
    return  lst2

def partition(lst,l,r):
    x=lst[r]
    i=1
    for j in range(l,r-1,1):
        if lst[j] <= x:
            swap(lst,i,j)
            i+=1

    swap(lst,i,r)
    return i

def fSelectHelper(lst,l,r,k):

    if k>0 and k<=r-l+1:
        idx=partition(lst,l,r)
        if idx-l==k-1:
            return lst[idx]
        elif idx-l>k-1:
            return fSelectHelper(lst,l,idx-1,k)
        else:
            return fSelectHelper(lst,idx+1,r,k-idx+l-1)


def fSelect(lst,idx):
    n = len(lst)-1
    return fSelectHelper(lst,0,n,idx)

def main():
    a=[10, 4, 5, 8, 6, 11, 26]
    print(fSelectHelper(a,6))
    print(max2(1.5,1.9))
main()
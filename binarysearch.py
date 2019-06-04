


def binary_iterative(a,num):

    l = 0
    ar = a
    r = len(ar)-1
    
    while 1:

     mid = l + (r-l)/2
     if r < l:
        return -1

     if ar[mid] == num:
         return mid

     if ar[mid] > num:
        r = mid - 1

     if ar[mid] < num:
        l = mid + 1



def binary_recursive(a,l,r,num):

    mid = l + (r-l)/2

    if r < l :
        return -1

    if a[mid] == num :
        return mid

    if a[mid] > num:
        binary_recursive(a,l,mid-1,num)


    if a[mid] < num:
       binary_recursive(a,mid+1,r,num)



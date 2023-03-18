#Compresion b/w binary and naive(linear) search ..!
import random
import time

def naiveSearch(lst,target):
    for i in  lst:
        if target==lst[i]:
           return i
    return -1

def binarySearch(lst,target,low=None,high=None):
    if low==None:
        low=0
    if high==None:
        high=len(lst)-1
    if high<low:
        return -1
    
    middle = (low+high)//2
    #base case
    if lst[middle] == target:
        return middle
    elif lst[middle] < target:
        return binarySearch(lst,target,middle+1,high)
    else:
        return binarySearch(lst,target,low,middle-1)


if __name__ == "__main__":
    length=10000
    lst = set()
    for i in range(length):
        lst.add(random.randint(-3*1000,3*1000))
    lst = sorted(list(lst))   
    start = time.time()
    for i in lst:
       naiveSearch(lst,lst)
    end = time.time()
    
    print("time taken by linear search is :",(end-start)/length," sec's")
    
    start = time.time()
    for i in lst:
       binarySearch(lst,lst[i])
    end = time.time()

    print("time taken by binary search is :",(end-start)/length," sec's")

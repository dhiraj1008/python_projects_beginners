# binary search algorithm by loop ..!

def binary_search(lst,key):
     low=0;
     high=len(lst)
     while low<=high:
        mid = (low+high)//2
        if lst[mid]==key:
            return mid
        elif lst[mid] < key:
            low=mid+1
        else:
            high=mid-1
     return -1

#list must be sorted in descending order..! 
lst = [1,2,3,4,5,6]
ind = binary_search(lst,1)
if ind!=-1:
    print("element found at :",ind," index")
else:
    print("element not found")
            
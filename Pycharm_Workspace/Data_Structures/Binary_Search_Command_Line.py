
import sys

def binary_search(lst,lb,ub,key):
    lst = sorted(lst)
    if lb < ub:
        mid = lb+(ub-lb)//2
        if lst[mid] == key:
            return mid
        elif key < lst[mid]:
            return binary_search(lst,lb,mid+1,key)
        else:
            return binary_search(lst,mid + 1,ub, key)
    return -1

lst = [5,4,3,2,1,32,45,67,86,34,22,11,33,46]
srch = binary_search(lst,0,len(lst),int(sys.argv[1]))
if srch!=-1:
    print(f"Element Found at {srch}")
else:
    print(f"Element Not Found...")

## In Pycharm right top      and   left to    run button     click on drop down list in that click on EDIT CONFIGURATIONS
## Then a window appears, and you will see parameters option there you specify the key element

## Using CMD
# open cmd and go through the path where your python exists then specify the path by mentioning    cd yourpath click enter
# now mention        python space filename.py keyvalue     click enter now
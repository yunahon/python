# Recursive

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high+low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


# Iterative Binary Search Function 
# It returns index of x in given array arr if present, 
# else returns -1 
def binary_search2(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        # Check if x is present at mid 
        if arr[mid] < x: 
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif arr[mid] > x: 
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            return mid 
  
    # If we reach here, then the element was not present 
    return -1
  
  
# Test array 
arr = [ 2, 3, 4, 9, 10, 40 ] 
x = 10
  
# Function call 
result = binary_search(arr, 0, len(arr)-1, x) 
result2 = binary_search2(arr, x) 

if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 

if result2 != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 
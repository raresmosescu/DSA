# Binary search generalized
# Doesn't include the -1 case where it is not found
def binary_search(array) -> int:

    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left != right:
        mid = left + (right - left) // 2
        
        # when the array value at mid is equal to the target value this has to be true as right has to include the target value
        # it could've easily been the other way around and used the left variable to include the target value
        if condition(mid): 
            right = mid 
        else:
            left = mid + 1

    # if not found still returns right
    return right # doesn't matter what you return here as left & right are equal at this point
 


# Example
def binary_search(array, n) -> int:

    left, right = 0, len(array)
    while left != right:
        mid = left + (right - left) // 2
        print(left,right, right-left, mid)
        print(n, array[mid], array[left:right+1], '\n')
        if array[mid] >= n:
            right = mid 
        else:
            left = mid + 1
    return right

print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], ))
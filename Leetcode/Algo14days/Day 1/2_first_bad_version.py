x = [True, True, True, True] + [False] * 123
x = [False]
x = [False, False]

def isBadVersion(n):
    if n<1:
        raise ValueError('n can\'t be less than 1)')
    return False if x[n-1] else True

# print(isBadVersion(3))
# print(isBadVersion(5))
# print(isBadVersion(4))


def firstBadVersion(n: int) -> int:

    if n == 1: return 1

    low = 1
    high = n
    mid = (low + high) // 2
    r = [isBadVersion(mid), isBadVersion(mid+1)]
    while low != high:
        if r == [False, False]:
            # this means that the bad version starts on the right half of the array
            low = mid + 1
        elif r == [True, True]:
            # this means that the bad version starts in the left half of the array
            high = mid
        elif r == [False, True]:
            return mid + 1
       
        mid = (low + high) // 2
        
        r = [isBadVersion(mid), isBadVersion(mid+1)]
        print(r, low, high, mid)
    
    if r == [True, True]:
        # this means that the bad version starts at mid +1 (False value)
        return 1 
    else:
        return -1
            



print(firstBadVersion(len(x)))



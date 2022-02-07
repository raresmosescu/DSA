from math import floor
from typing import List


nums = [-1,0,3,5,9,12]


def search(nums: List[int], target: int) -> int:

    low = 0
    high = len(nums) - 1
    mid = (low + high) // 2
    
    while high != low:

        if target <= nums[mid]:
            # when target is on the left half
            high = mid
        elif target > nums[mid]:
            # when target is on the right half
            low = mid + 1
        
        mid = (low + high) // 2

    if nums[mid] == target:
        # when target is right in the middle 
        return mid
    else:
        return -1

# print(search(nums, 9))
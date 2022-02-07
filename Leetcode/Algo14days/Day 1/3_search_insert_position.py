from typing import List

def searchInsert(self, nums: List[int], target: int) -> int:
        
    low = 0
    high = len(nums)
    
    while (low != high):
        mid = low + (high-low) // 2
        
        if target <= nums[mid]:
            high = mid
        else:
            low = mid + 1
    
    return high
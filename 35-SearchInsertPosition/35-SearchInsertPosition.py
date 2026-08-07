# Last updated: 07/08/2026, 12:12:49
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
                if nums[i] >= target:
                    return i
        return len(nums) 
        
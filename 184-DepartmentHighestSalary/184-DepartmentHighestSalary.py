# Last updated: 07/08/2026, 12:12:20
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3
4        for i in range(len(nums)):
5                if nums[i] >= target:
6                    return i
7        return len(nums) 
8        
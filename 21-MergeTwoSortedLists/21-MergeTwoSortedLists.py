# Last updated: 29/07/2026, 23:12:05
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3
4        k = 1
5        for i in range(1, len(nums)):
6            if nums[i] != nums[k - 1]:
7                nums[k] = nums[i]
8                k += 1
9        return k
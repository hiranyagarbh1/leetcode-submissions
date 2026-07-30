# Last updated: 29/07/2026, 23:12:26
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k
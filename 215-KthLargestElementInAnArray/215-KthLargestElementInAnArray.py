# Last updated: 28/07/2026, 22:16:17
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # for i in range(k-1):

        #     nums.remove(max(nums))
        
        # return max(nums)

        n = len(nums)

        nums_sorted = sorted(nums)

        return nums_sorted[n-k]
        
# Last updated: 28/07/2026, 22:16:23
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in seen:

                return [seen[complement], i]
                
            seen[num]=i

        
        
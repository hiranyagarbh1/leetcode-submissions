# Last updated: 28/07/2026, 22:16:21
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        result = 0
        
        for num in nums:
            result ^= num
        
        return result

        # frequencies = Counter(nums)

        # for num, count in frequencies.items():

        #     if count==1:
        #         return num
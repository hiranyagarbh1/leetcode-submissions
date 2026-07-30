# Last updated: 29/07/2026, 23:12:25
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for element in range(len(nums)):
            if nums[element]!=val:
                nums[k]=nums[element]
                k+=1
        return k




        
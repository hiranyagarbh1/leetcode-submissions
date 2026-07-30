# Last updated: 29/07/2026, 23:03:17
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        k=0
4        for element in range(len(nums)):
5            if nums[element]!=val:
6                nums[k]=nums[element]
7                k+=1
8        return k
9
10
11
12
13        
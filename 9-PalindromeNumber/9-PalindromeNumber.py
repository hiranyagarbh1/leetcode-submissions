# Last updated: 28/07/2026, 22:16:22
class Solution:
    def isPalindrome(self, x: int) -> bool:

        strx=str(x)

        return strx==strx[::-1]
        
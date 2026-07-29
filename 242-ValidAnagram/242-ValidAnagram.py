# Last updated: 28/07/2026, 22:16:19
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        
        return sorted(s)==sorted(t)
        


    
        
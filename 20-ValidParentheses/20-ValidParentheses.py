# Last updated: 29/07/2026, 22:46:14
1class Solution:
2    def isValid(self, s: str) -> bool:
3
4        prev_length=-1
5
6        while len(s)!=prev_length:
7               
8               prev_length = len(s)
9
10               s=s.replace('()','').replace('{}', '').replace('[]','')
11    
12        return len(s)==0
13        
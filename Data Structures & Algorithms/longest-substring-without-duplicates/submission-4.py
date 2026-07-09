class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        res = 0
        for i in range(len(s)):
            newset = set()
            for j in range(i,len(s)):
                if s[j] in newset:
                    break

                newset.add(s[j])    
            length = len(newset)
            res = max(length,res)
        return res    




        
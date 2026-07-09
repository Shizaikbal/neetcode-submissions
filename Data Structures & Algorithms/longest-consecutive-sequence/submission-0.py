class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newset = set(nums)
        res = 0
        for i in newset:
            if(i-1) not in newset:
                len = 1
                while(i + len) in newset:
                    len += 1
                res = max(len,res)
        return res            

        
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            lm = rm = height[i]

            for j in range(i):
                lm = max(lm,height[j])

            for j in range(i+1,len(height)):
                rm = max(rm,height[j])

            res += min(lm,rm) - height[i]

        return res

        
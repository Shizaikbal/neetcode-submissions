class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

sol = Solution()
result = sol.getConcatenation([3,1,1,5])
print(result)        
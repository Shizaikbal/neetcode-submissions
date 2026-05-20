class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicates = len(nums) != len(set(nums))
        if has_duplicates:
            return True
        else:
            return False
sol = Solution()
result = sol.hasDuplicate([1,1,3,4])   
print(result)         
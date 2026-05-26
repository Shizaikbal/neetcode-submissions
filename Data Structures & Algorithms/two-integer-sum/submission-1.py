class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i , num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement],i]

            seen[num] = i    
sol = Solution()
sol.twoSum([3,4,5,6],7)                                                                                      
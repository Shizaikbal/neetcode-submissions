class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i , num in enumerate(numbers):
            complement = target - num

            if complement in seen and (seen[complement] < i):
                return [seen[complement] +1, i+1]
            else :
                seen[num] = i 
        return []           
        
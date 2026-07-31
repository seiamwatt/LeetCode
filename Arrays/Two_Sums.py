class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution_map = {}

        for i,num in enumerate(nums):
            val = target - num
            
            if val in solution_map:
                return [solution_map[val],i]
            
            solution_map[num] = i


        
            
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        if(len(nums) == 1):
            return nums[0]
        
        last_index = None
        
        

        for index in range(len(nums) - 1):
            

            if(nums[index] == last_index):
                continue

            last_index = nums[index ]
            
            if(nums[index] != nums[index + 1]):
                return nums[index]
            

            

        return nums[-1]
    

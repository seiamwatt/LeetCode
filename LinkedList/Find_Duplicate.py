class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        temp_map = {}

        for num in nums:
            if num in temp_map:
                temp_map[num] += 1
            else:
                temp_map[num] = 1

                
        for element in temp_map:
            if(temp_map[element] >= 2):
                return element

        return 0
        

        
# nums = [3,2,4], target = 6


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_hashMap = {}
        output_list = []

        for index,num in enumerate(nums):
            difference = target - num

            if(difference in nums_hashMap):
                output_list.append(index)
                output_list.append(nums_hashMap[difference])
                return output_list
            
            nums_hashMap[num] = index


        return output_list
            

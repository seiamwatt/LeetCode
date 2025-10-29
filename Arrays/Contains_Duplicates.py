class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        init_array_length = len(nums)

        set_of_nums = set(nums)

        if(len(nums) > len(set_of_nums)):
            return True
        

        return False
        
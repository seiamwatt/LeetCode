class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list_len = len(nums)

        no_dup_list_len = len(set(nums))

        if list_len != no_dup_list_len:
            return True 

        return False
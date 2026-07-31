class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_list = []

        for num in nums:
            if num in nums_list:
                return num

            nums_list.append(num)
        
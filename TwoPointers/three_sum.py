class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        target = 0
        sorted_nums = sorted(nums)
        results = []

        for i in range(len(sorted_nums)):

            left_pointer = i + 1
            right_pointer = len(sorted_nums) - 1

            if i > 0 and sorted_nums[i] == sorted_nums[ i - 1]:
                continue

            while left_pointer < right_pointer:
                sum = sorted_nums[i] + sorted_nums[left_pointer] + sorted_nums[right_pointer]

                if sum == target:
                    prev_num = sorted_nums[left_pointer]
                    results.append([sorted_nums[i],sorted_nums[left_pointer],sorted_nums[right_pointer]])
                    left_pointer += 1

                    while left_pointer < right_pointer and (sorted_nums[left_pointer] == prev_num):
                        left_pointer += 1

                if sum < target:
                    prev_num = sorted_nums[left_pointer]
                    left_pointer +=1
                    while left_pointer < right_pointer and (sorted_nums[left_pointer] == prev_num):
                        left_pointer += 1

                if sum > target:
                    prev_num = sorted_nums[right_pointer]
                    right_pointer -= 1
                    while left_pointer < right_pointer and (sorted_nums[right_pointer] == prev_num):
                        right_pointer -= 1
        return results 
        
        
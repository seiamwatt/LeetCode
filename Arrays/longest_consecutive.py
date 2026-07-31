class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest_count = 0

        for num in num_set:
            if (num - 1) not in num_set:
                count = 1

                while (num + count) in num_set:
                    count += 1

                if count > longest_count:
                    longest_count = count

        
        return longest_count
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        new_list = list(set(nums))
        new_list.sort()
        highest_sequence_count = 0
        curr_sequence_count = 0

        if(len(new_list) == 1):
             return 1

        for i in range(len(new_list) - 1):
            if(new_list[i] + 1 == new_list[i + 1]):
                curr_sequence_count += 1
                continue

            if curr_sequence_count >= highest_sequence_count:
                curr_sequence_count += 1
                highest_sequence_count = curr_sequence_count 

            curr_sequence_count = 0

        
        if curr_sequence_count >= highest_sequence_count:
                curr_sequence_count += 1
                highest_sequence_count = curr_sequence_count
                
        return highest_sequence_count

def main():
    solution = Solution()
    print("test")
    print(solution.longestConsecutive([1,100]))



if __name__ == "__main__":
    main()
        

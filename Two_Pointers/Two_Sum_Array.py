from typing import List
class Solution:
    # returns the 2 index
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_hashMap = {}

        output_list = []

        for index,num in enumerate(numbers):
            difference = target - num

            if(difference in nums_hashMap):
                 print(nums_hashMap[difference])
                 return [nums_hashMap[difference] + 1,index + 1]
                #  output_list.append()
               
        
            nums_hashMap[num] = index


        return output_list
        






   
def main():
    # Your code here
    solution = Solution()
    solution.twoSum([2,7,11,15],9)

if __name__ == "__main__":
    main()
        

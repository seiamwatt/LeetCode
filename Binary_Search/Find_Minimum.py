class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        nums.sort()

        return nums[0]




    
    def binarySearch(self,nums: List[int],target:int) -> bool:

        low = 0
        high = len(nums) - 1

        while(low <= high):
            middle = low + (high - low) // 2

            if(nums[middle] == target):
                return True
            
            elif(nums[middle] < target):
                 low = middle + 1 

            elif(nums[middle] > target):
                high = middle - 1

        return False


        
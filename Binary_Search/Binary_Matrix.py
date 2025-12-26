class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for element in matrix:
            if self.binarySearch(element,target):
                return True
        
        return False
        

    
    # helper
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


        
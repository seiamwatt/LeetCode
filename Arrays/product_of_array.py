class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_temp = 1
        prefix = []

        for index, num in enumerate(nums):
            prefix.append(prefix_temp)  
            prefix_temp = prefix_temp * num


        postfix_temp = 1
        temp_postfix_list = []
        
        for index, num in enumerate(reversed(nums)): 
            temp_postfix_list.append(postfix_temp)  
            postfix_temp = postfix_temp * num 

        postfix = list(reversed(temp_postfix_list))


        output = [] 

        for index, num in enumerate(nums):
            product = prefix[index] * postfix[index]  
            output.append(product)


        return output
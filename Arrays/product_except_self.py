class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prev_num =1 

        for num in nums:
            prefix.append(prev_num * num)
            prev_num = prev_num * num

        reverse_list = reversed(nums)

        postfix = []
        prev_num = 1
        for num in reverse_list:
            postfix.append(prev_num * num)
            prev_num = prev_num * num 

        
        postfix = postfix[::-1]

        output_list = []
        for i in range(len(nums)):
            if i > 0:
                left = prefix[i - 1]
            else:
                left = 1

            if i < len(nums) - 1:
                right = postfix[i+1]
            else:
                right = 1

            output_list.append(left*right)

        return output_list
    


            




         

        

         
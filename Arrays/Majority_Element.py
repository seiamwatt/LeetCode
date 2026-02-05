class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_dict = {}
        highest_element_count = 0
        majority_element = 0

        for element in nums:
            element_dict[element] = 0

        
        for element in nums:
            element_dict[element] += 1


        for element in nums:
            if element_dict[element] > highest_element_count:
                highest_element_count = element_dict[element]
                majority_element = element


        return majority_element
       
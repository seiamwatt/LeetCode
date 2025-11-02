from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        count = defaultdict(int)

        if(len(nums) == 1 and k == 1):
            results.append(nums[0])
            return results
        
        for num in nums:
            count[num] += 1


        sorted_elements = sorted(count,key = lambda x: count[x],reverse=True)[:k]

        for element in sorted_elements:
            results.append(element)
        
        return results
        
        

        
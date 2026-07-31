class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        solution_map = {}

        for num in nums:
            if num not in solution_map:
                solution_map[num] = 0

        for num in nums:
            if num in solution_map:
                solution_map[num] += 1

        sorted_dict = dict(sorted(solution_map.items(),reverse=True)[:k])
        
        output_list = []
        for key in sorted_dict:
            output_list.append(key)

        return output_list
            





            


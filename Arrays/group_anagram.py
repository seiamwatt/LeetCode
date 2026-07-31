class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution_map = {}

        temp_list = []
        
        for word in strs:
            temp = ''.join(sorted(word)) 
            temp_list.append(temp)

        temp_list = set(temp_list)

        for word in temp_list:
            solution_map[word] = []

        for word in strs:
            temp = ''.join(sorted(word))
            if temp in solution_map:
                solution_map[word].append(temp)

        output_list = []
        for value in solution_map.values:
            output_list.append(value)

        return output_list



            



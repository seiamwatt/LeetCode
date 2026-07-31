class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []

        for letter in s:
            s_list.append(letter)
        
        for letter in t:
            t_list.append(letter)

        if sorted(s_list) == sorted(t_list):
            return True
        return False
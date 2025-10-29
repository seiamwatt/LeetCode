class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_array = []
        t_array = []
        
        for word in s:
            s_array.append(word)

        for word in t:
            t_array.append(word)

        list.sort(s_array)
        list.sort(t_array)

        if(s_array == t_array):
            return True
        
        return False


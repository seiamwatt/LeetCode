class Solution:
    def isValid(self, s: str) -> bool:
       
        stack = []

        map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
       
        if len(s) == 1:
            return False
       
        for element in s:
            if element in "({[":
                stack.append(element)

            elif element in ")}]":
                temp = None
                if(len(stack) >= 1):
                    temp = stack.pop()

                if map[element] != temp:
                    return False
        
        if (len(stack) != 0):
            return False
               
        return True
  
def main():
    # Your code here
    solution = Solution()
    solution.isValid("(")

if __name__ == "__main__":
    main()
        

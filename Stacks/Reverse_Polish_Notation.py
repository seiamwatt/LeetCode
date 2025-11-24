class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_nums  = []
        curr_val = None

        for token in tokens:

            if(token not in ["+","-","/","*"]):
                stack_nums.append(int(token))
            else:
                
                if(token == "+"):
                    temp1 = stack_nums.pop()
                    temp2 = stack_nums.pop()
                    stack_nums.append(temp1 + temp2)

                elif(token == "-"):
                    temp1 = stack_nums.pop()
                    temp2 = stack_nums.pop()
                    stack_nums.append(temp2 - temp1)

                elif(token == "/"):
                    temp1 = stack_nums.pop()
                    temp2 = stack_nums.pop()
                    stack_nums.append(int(temp2 / temp1))

                elif(token == "*"):
                    temp1 = stack_nums.pop()
                    temp2 = stack_nums.pop()
                    stack_nums.append(temp1 * temp2)


        return stack_nums.pop()
                    


                    




            



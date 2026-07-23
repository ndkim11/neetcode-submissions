class Solution:
    def calculate(self,num1:int,num2:int, operand):
        if operand == '+':
            return num1+num2

        elif operand == '-':
            return num1-num2

        elif operand == '*':
            return num1*num2

        elif operand == '/':
            return int(num1/num2)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = ['+','-','*','/']
        for token in tokens:
            # there are two elements in stack when operand comes in
            if token in operand:
                if len(stack) > 1:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    res = self.calculate(num1,num2,token)
                    stack.append(res)
                else:
                    return 
            else:
                stack.append(int(token))

        return stack[-1]
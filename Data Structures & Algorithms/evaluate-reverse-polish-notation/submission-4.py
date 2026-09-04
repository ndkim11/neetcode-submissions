import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operand = {
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/': lambda a,b: int(a/b)
        }

        for t in tokens:
            if t in operand:
                b, a = int(s.pop()), int(s.pop())
                s.append(operand[t](a,b))

            else:
                s.append(t)

        return int(s.pop())

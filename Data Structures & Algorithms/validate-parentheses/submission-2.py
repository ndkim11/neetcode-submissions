class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        par_dict = {'(':')','{':'}','[':']'}

        for c in s:
            if c in par_dict:
                stack.append(c)

            else:
                if not stack or par_dict[stack[-1]] != c:
                    return False
                stack.pop()

        return not stack
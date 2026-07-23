class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        [1,4][4,6][7,8][10,10]
        [4107][6318][8529][10,7,3,10]
        make a pair and sort
        '''
        cars = sorted(zip(position,speed),reverse=True)
        stack=[]

        for p,s in cars:
            eta = (target-p)/s
            stack.append(eta)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
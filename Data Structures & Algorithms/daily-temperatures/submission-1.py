class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        [30] <- 38 => 30<- [38] => [38,30] <- 36 => 30<-[38,36]
        '''
        stack = []
        answer = [0]*len(temperatures)
        
        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _,idx = stack.pop()
                answer[idx]=i-idx

            stack.append((temp,i))

        while stack:
            _, idx = stack.pop()
            answer[idx]=0

        # print(answer)
        return answer
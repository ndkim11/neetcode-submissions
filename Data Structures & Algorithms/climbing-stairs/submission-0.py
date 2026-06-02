class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        2 = 1 + 1
        3= 1+2 = 2+1 = 1+1+1
        '''
        visited = [0]*(n+1)

        for i in range(1,n+1):
            if i == 1:
                visited[i]=1
                continue
            if i == 2:
                visited[i]=2
                continue
            visited[i]=visited[i-1]+visited[i-2]

        return visited[n]
            
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0]*numCourses

        for adv, pre in prerequisites:
            adj[pre].append(adv)
            in_degree[adv] += 1

        # 선수 과목이 없는(in-degree==0) 과목부터 큐에 삽입
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        taken_courses = 0

        while queue:
            cur = queue.popleft()
            taken_courses += 1
            
            for nxt in adj[cur]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)
        
        return taken_courses == numCourses

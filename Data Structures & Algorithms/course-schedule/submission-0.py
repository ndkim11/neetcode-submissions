class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0: unvisited 1: ing 2:done
        states = [0]*numCourses
        courses=[[] for _ in range(numCourses)]  #[ [],[],[]...[] ]

        for adv,pre in prerequisites:
            courses[pre].append(adv)

        def has_cycle(node: int) -> bool:
            if states[node] == 1: # 탐색 중인 노드가 다시 나왔음
                return True
            if states[node] == 2:
                return False

            states[node] = 1
            for nxt in courses[node]:
                if has_cycle(nxt):
                    return True

            states[node] = 2
            return False

        for i in range(numCourses):
            if states[i]==0:
                if has_cycle(i):
                    return False

        return True
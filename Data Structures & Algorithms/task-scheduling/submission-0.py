class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) #count each?
        maxHeap = [-count for count in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap: #heap is empty --> nothing to do
                time = q[0][1]

            else:
                cnt = 1 + heapq.heappop(maxHeap) # -(cnt-1)
                if cnt: #cnt is not 0; no need to add to queue if 0: No more task need done
                    q.append([cnt, time + n]) # when is it available

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
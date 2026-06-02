class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = list(nums) # Fresh copy
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

        self.size = len(self.minHeap)

    def add(self, val: int) -> int:
        if self.size < self.k:
            heapq.heappush(self.minHeap, val)
            self.size += 1
        elif val > self.minHeap[0]: # bigger val is inserted and heap is bigger than k
            heapq.heapreplace(self.minHeap, val)

        return self.minHeap[0]
import heapq


class MaxHeap:
    def __init__(self, ELEMENTS):
        self.heap = []
        [self.push(e) for e in ELEMENTS]

    def push(self, item):
        heapq.heappush(self.heap, (-item[0], item))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def peek(self):
        return self.heap[0][1]

    def __list__(self):
        return [item[1] for item in self.heap]

    def __len__(self):
        return len(self.heap)

    def all(self):
        elements = [e[1] for e in self.heap]
        return elements

    def clean(self):
        self.heap = []

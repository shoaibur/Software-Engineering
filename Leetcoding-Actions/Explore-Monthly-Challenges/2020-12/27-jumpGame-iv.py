class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        d = collections.defaultdict(list)
        for index, element in enumerate(arr):
            d[element].append(index)

        queue = collections.deque([(0, 0)])
        s = set()
        s.add(0)

        while len(queue):
            currIndex, jumps = queue.popleft()

            for nextIndex in [currIndex + 1, currIndex - 1] + d[arr[currIndex]][::-1]:
                if nextIndex < len(arr) and nextIndex > -1 and nextIndex != currIndex and nextIndex not in s:
                    if nextIndex == len(arr) - 1:
                        return jumps + 1
                    s.add(nextIndex)
                    queue.append((nextIndex, jumps + 1))

        return -1
